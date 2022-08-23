from events_processing import (get_matches,
                               get_teams,
                               get_players,
                               get_player_statistics)
from helpers import (save_to_jsonlines,
                     get_user_input)
import pandas as pd

# Getting the path to the input data csv file
events_csv = get_user_input()

# Turning the data to Dataframe Format and validating if all needed columns are present
events = pd.read_csv(events_csv)

# Calling the functions for each output dataframe and saving it to jsonlines format
save_to_jsonlines(get_matches(events), 'Match')
save_to_jsonlines(get_teams(events), 'Team')
save_to_jsonlines(get_players(events), 'Player')
save_to_jsonlines(get_player_statistics(events), 'Player Statistics')

