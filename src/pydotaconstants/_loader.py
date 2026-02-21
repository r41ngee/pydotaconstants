import pickle
from importlib import resources

with resources.files("pydotaconstants.data").joinpath("heroes.pkl").open("rb") as f:
    _HEROES: dict = pickle.load(f)

with resources.files("pydotaconstants.data").joinpath("abilities.pkl").open("rb") as f:
    _ABILITIES: dict = pickle.load(f)

with resources.files("pydotaconstants.data").joinpath("locals.pkl").open("rb") as f:
    _LOCALS: dict = pickle.load(f)