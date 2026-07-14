# PyDotaConstants

PyDotaConstants is a Python library that provides structured access to Dota 2 hero, ability, and item data.

## Installation

```bash
pip install pydotaconstants
```

## Quick Start

```python
from pydotaconstants import Hero, Ability, Item

# Get hero by codename
hero = Hero.getByName("npc_dota_hero_axe")
print(hero.displayName)  # Axe

# Get hero by display name
hero = Hero.getByDisplayName("Axe")
print(hero.id)  # 2

# Get ability by display name
ability = Ability.getByDisplayName("Blink")
print(ability.displayDescription)

# Get item by codename
item = Item.getByName("item_blink")
print(item.displayName)  # Blink Dagger

# List all heroes
for hero in Hero.all():
    print(hero.displayName)
```

## API Reference

- [Heroes](api/heroes.md) — `Hero` class reference
- [Abilities](api/abilities.md) — `Ability` class reference
- [Items](api/items.md) — `Item` class reference

## Data Browser

Browse the raw Dota 2 data directly:

- [Heroes Browser](data/heroes.html)
- [Abilities Browser](data/abilities.html)
- [Items Browser](data/items.html)

## Configuration

The library bundles pre-compiled data files in `src/pydotaconstants/data/`:

| File | Description |
|------|-------------|
| `heroes.json` / `heroes.pkl` | All Dota 2 heroes |
| `abilities.json` / `abilities.pkl` | All Dota 2 abilities |
| `items.json` / `items.pkl` | All Dota 2 items |
| `locals.json` / `locals.pkl` | Localization strings |

## License

MIT License — see [LICENSE](https://github.com/r41ngee/pydotaconstants/blob/main/LICENSE) for details.
