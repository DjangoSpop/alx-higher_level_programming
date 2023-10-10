#!/usr/bin/python3
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Name of the JSON file
json_filename = "add_item.json"

# Check if the JSON file exists, and load its contents if it does
if os.path.exists(json_filename):
    my_list = load_from_json_file(json_filename)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, json_filename)
