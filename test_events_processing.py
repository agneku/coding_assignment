import pandas as pd
from pandas.testing import assert_frame_equal
from events_processing import (get_matches,
                               get_teams,
                               get_players,
                               get_player_statistics)

mock_data = {'match_id': [814, 1217, 1217, 814],
             'match_name': ['Match 1', "Match 2", "Match 2", "Match 1"],
             'team_id': [14, 17, 18, 12],
             'team_name': ['Team 1', 'Team 2', 'Team 3', 'Team 4'],
             'is_home': [True, True, False, False],
             'player_id': [153, 196, 200, 120],
             'player_name': ["Thomas", "Trevor", "Jim", "James"],
             'goals_scored': [1, 1, 1, 1],
             'minutes_played': [72, 78, 51, 46]}

test_input = pd.DataFrame(mock_data)


def test_match_processing():
    match_data = {'match_id': [814, 1217],
                  'match_name': ["Match 1", "Match 2"],
                  'home_team_id': [14, 17],
                  'away_team_id': [12, 18],
                  'home_goals': [1, 1],
                  'away_goals': [1, 1]}

    match_expected_df = pd.DataFrame(match_data)
    match_result_df = get_matches(test_input)

    assert_frame_equal(match_result_df, match_expected_df)


def test_team_processing():
    team_data = {'team_id': [12, 14, 17, 18],
                 'team_name': ['Team 4', 'Team 1', 'Team 2', 'Team 3']}

    team_expected_df = pd.DataFrame(team_data)
    team_result_df = get_teams(test_input)

    assert_frame_equal(team_result_df, team_expected_df)


def test_player_processing():
    player_data = {'player_id': [120, 153, 196, 200],
                   'team_id': [12, 14, 17, 18],
                   'player_name': ["James", "Thomas", "Trevor", "Jim"]}

    player_expected_df = pd.DataFrame(player_data)
    player_result_df = get_players(test_input)

    assert_frame_equal(player_result_df, player_expected_df)


def test_statistic_processing():
    statistic_data = {'stat_id': [0, 1, 2, 3],
                      'player_id': [153,  120, 196, 200],
                      'match_id': [814, 814, 1217, 1217],
                      'goals_scored': [1, 1, 1, 1],
                      'minutes_played': [72, 46, 78, 51],
                      'fraction_of_total_minutes_played': [0.8, 0.511111, 0.866667, 0.566667],
                      'fraction_of_total_goals_scored': [0.5, 0.5, 0.5, 0.5]}

    statistic_expected_df = pd.DataFrame(statistic_data)
    statistic_result_df = get_player_statistics(test_input)

    assert_frame_equal(statistic_result_df, statistic_expected_df)
