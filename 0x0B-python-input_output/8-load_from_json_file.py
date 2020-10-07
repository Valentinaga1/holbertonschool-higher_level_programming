#!/usr/bin/python3
import json
""""Module to define a creation of an object from a JSON
"""


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”

    Args:
        filename (str): text file to read.

    Returns:
        Returns an object
    """
    with open(filename) as f:
        return json.load(f)