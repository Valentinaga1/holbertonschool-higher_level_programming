#!/usr/bin/python3
""""Module to define a Python representation string function from JSON.
"""
import json


def from_json_string(my_str):
    """Function that returns an object represented by a JSON string

    Args:
        my_obj : object to convert from json

    Returns:
        A python representation from json
    """
    return json.loads(my_str)
