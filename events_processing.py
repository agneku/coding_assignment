import pandas as pd


def get_matches(events):
    """Transforms the input dataframe to show information about each match"""
    home_match_events = convert_to_match_events(events, True)
    away_match_events = convert_to_match_events(events, False)

    matches = pd.merge(home_match_events, away_match_events,
                       on=["match_id", "match_name"], how='outer')

    matches = matches[['match_id', 'match_name', 'home_team_id',
                       'away_team_id', 'home_goals', 'away_goals']]

    print('Match DataFrame created')
    return matches


def convert_to_match_events(events, is_home: bool):
    """Transforms the input dataframe to show total goals scored in each match per team(away or home)"""
    filtered_events = events[events['is_home'] == is_home]

    match_events = filtered_events.groupby(['match_id', 'match_name', 'team_id'],
                                            as_index=False).goals_scored.sum()

    if is_home:
        name = 'home'
    else:
        name = 'away'

    match_events.rename(columns={'goals_scored': name+'_goals', 'team_id': name+'_team_id'}, inplace=True)

    return match_events


def get_teams(events):
    """Transforms the input dataframe to show information about each team"""
    team_events = events.groupby(['team_id', 'team_name'], as_index=False)
    teams = pd.DataFrame(team_events.groups.keys(), columns=['team_id', 'team_name'])

    print('Team DataFrame created')
    return teams


def get_players(events):
    """Transforms the input dataframe to show information about each player"""
    player_events = events.groupby(['player_id', 'team_id', 'player_name'], as_index=False)
    players = pd.DataFrame(player_events.groups.keys(), columns=['player_id', 'team_id', 'player_name'])

    print('Player DataFrame created')
    return players


def get_player_statistics(events):
    """Transforms the input dataframe to show information about each players performance"""
    match_goals = get_match_goals(events)

    player_stats = pd.merge(events, match_goals, on=["match_id"], how='outer')

    player_stats['fraction_of_total_minutes_played'] = player_stats['minutes_played'] / 90
    player_stats['fraction_of_total_goals_scored'] = player_stats['goals_scored'] / player_stats['total_match_goals']
    player_stats['stat_id'] = player_stats.index

    player_stats = player_stats[['stat_id', 'player_id', 'match_id', 'goals_scored',
                                    'minutes_played', 'fraction_of_total_minutes_played',
                                    'fraction_of_total_goals_scored']]
    print('Player Statistics DataFrame created')
    return player_stats


def get_match_goals(events):
    """Gets total goals per match"""
    match_goals = events.groupby(['match_id'], as_index=False).goals_scored.sum()
    match_goals.rename(columns={'goals_scored': 'total_match_goals'}, inplace=True)
    return match_goals


