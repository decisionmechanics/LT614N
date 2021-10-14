import yaml


def to_yaml(data):
    return yaml.dump(data)


def from_yaml(text):
    return yaml.load(text)


text = to_yaml({"customer": "ARM", "course": "614N", "title": "Advanced Python"})
course = from_yaml(text)
