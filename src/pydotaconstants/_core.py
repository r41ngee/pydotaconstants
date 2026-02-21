import pickle
from importlib import resources

with resources.files("pydotaconstants.data").joinpath("heroes.pkl").open("rb") as f:
    HEROES = pickle.load(f)

with resources.files("pydotaconstants.data").joinpath("abilities.pkl").open("rb") as f:
    ABILITIES = pickle.load(f)

with resources.files("pydotaconstants.data").joinpath("locals.pkl").open("rb") as f:
    LOCALS = pickle.load(f)