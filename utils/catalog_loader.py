import json


def load_catalog():
    """
    Load SHL assessment catalog from JSON file
    """

    with open("data/shl_catalog.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data