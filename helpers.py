
def save_to_jsonlines(dataframe, name):
    """Saves a given dataframe to jsonlines format"""
    dataframe.to_json(name + '.jsonl', orient='records', lines=True)
    print(name + ' DataFrame was successfully saved to jsonlines format')


def get_user_input():
    """Gets a path to input data from the user"""
    input_data = input("Enter path to the input data csv file: \n")

    #  removing apostrophes in case the path is inserted as a string
    input_data = input_data.replace("'", "")
    input_data = input_data.replace('"', "")

    return input_data
