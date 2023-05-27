import json

INPUT_THEME_JSON = "themes.json"

def read_json_into_dict(input_json):
    # Read JSON data from a file
    with open(input_json) as json_file:
        json_data = json.load(json_file)

    map_data = {}

    for item in json_data:
        key = next(iter(item))  # Get the key from the dictionary
        value = item[key]  # Get the value associated with the key
        map_data[key] = value

    return map_data
