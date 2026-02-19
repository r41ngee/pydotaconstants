import json
from importlib import resources

with resources.files("pydotaconstants.data").joinpath("heroes.json").open(encoding="utf-8") as f:
    HEROES = json.load(f)