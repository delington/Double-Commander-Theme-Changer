import json


def read_themes_as_list(input_json):
    # Read JSON data from a file
    with open(input_json) as json_file:
        read_list = json.load(json_file)

    return read_list