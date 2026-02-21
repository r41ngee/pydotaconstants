# PyDotaConstants

PyDotaConstants is a Python library designed to provide structured access to Dota 2 hero and ability data. It allows developers to easily retrieve hero and ability information based on their code names and display names. This project is particularly useful for creating applications and tools that require detailed insights into Dota 2's capabilities and characters.

## Features
- Retrieve hero information by codename, ID, or display name.
- Access ability information similarly through codename or display name.
- Data is loaded from pre-compiled binary files, ensuring fast access and processing.
- Supports a structured schema for hero and ability data that can be easily navigated.

## Installation and Setup
To install the PyDotaConstants library, simply clone the repository and ensure the necessary data files are in place. The current data files must be compiled as `.pkl` files as represented in the `src/pydotaconstants/data` directory. 

```bash
git clone https://github.com/yourusername/pydotaconstants.git
cd pydotaconstants
```

Make sure to run the `_update.py` script to generate the necessary data files if they are not already provided.

```bash
python src/_update.py
```

## Basic Usage
To use the library, you can import the desired classes and access hero or ability data as shown below:

```python
from pydotaconstants import Hero, Ability

# Get hero by codename
hero = Hero.getByName("npc_dota_hero_axe")
print(hero.displayName)  # Output: Axe

# Get ability by display name
ability = Ability.getByDisplayName("Hex")
print(ability.displayDescription)
```

## Configuration
This library expects certain pre-compiled data files:
- `heroes.pkl`: Contains data for all Dota 2 heroes.
- `abilities.pkl`: Contains data for all Dota 2 abilities.
- `locals.pkl`: Contains localization strings for heroes and abilities.

Make sure these files are located in the `src/pydotaconstants/data` directory for the library to function correctly.

## Contributing Guidelines
Contributions to PyDotaConstants are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request detailing your changes.

Please ensure any new features include tests and documentation updates as necessary.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.