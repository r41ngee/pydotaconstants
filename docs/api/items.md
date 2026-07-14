# Item

```python
from pydotaconstants import Item
```

The `Item` class represents a single Dota 2 item. Do not instantiate directly — use the class methods below.

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | `str` | Item codename, e.g. `item_blink` |
| `displayName` | `str` | Localized name, e.g. `Blink Dagger` |
| `data` | `dict` | Raw item data dictionary |

## Methods

### `Item.getByName(name)`

Get an item by its codename.

```python
item = Item.getByName("item_blink")
print(item.displayName)  # Blink Dagger
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Item codename |

**Returns:** `Item`

---

### `Item.getByDisplayName(display_name)`

Get an item by its display name.

```python
item = Item.getByDisplayName("Blink Dagger")
print(item.name)  # item_blink
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `display_name` | `str` | Item display name (English) |

**Returns:** `Item`

**Raises:** `IndexError` — if the display name is not found.

---

### `Item.all()`

Get all items.

```python
items = Item.all()
print(len(items))  # 200+
```

**Returns:** `list[Item]`
