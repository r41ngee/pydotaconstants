import json
from importlib import resources

with resources.files("pydotaconstants.data").joinpath("heroes.json").open(encoding="utf-8") as f:
    HEROES = json.load(f)

with resources.files("pydotaconstants.data").joinpath("abilities.json").open(encoding="utf-8") as f:
    ABILITIES = json.load(f)

with resources.files("pydotaconstants.data").joinpath("locals.json").open(encoding="utf-8") as f:
    LOCALS = json.load(f)