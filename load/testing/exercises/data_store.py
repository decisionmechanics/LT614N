import json


def load_data():
    try:
        with open("small.json") as f:
            return json.load(f)
    except MemoryError:
        return []
