# RPG Hero

## Specyfication

### Classes:

#### Character
basic info about our hero

#### Attributes:
* `first_name`
* `last_name`
* `race`

#### Methods:

##### `__str__`

#### Item
Represents an item that hero can put into inventory

#### Attributes:
* `name`
* `description`
* `weight`

#### Inventory
represents hero's inventory

#### Attributes:
* `capacity` - max number of items that can be stored in the inventory
* `max_weight` - max weight that can be stored in the inventory
* `items` - list of items

#### Methods:

##### `add_item(item)`
Adds item to the inventory, but first checks if it's possible (capacity or max_weight are not reached)

##### `drop_item(item)` 
Removes item from the inventory

##### `get_inventory_size()` 
Returns number of items in the inventory

##### `get_inventory_weight()` 
Returns total weight of all items in the inventory

##### `get_the_heaviest_item()` 
Return the heaviest item in the inventory

#### Hero
represents our hero

#### Attributes:
* `character` - Character object
* `inventory` - Inventory object
* `experience`
* `level`

#### Methods:

##### `__init__(firs_name, last_name, race)` 
Creates an hero instance

##### `get_items()` 
Returns list of items in hero's inventory

##### `pick_an_item(item)` 
Adds item to the inventory

##### `drop_item(item)` 
Removes item from the inventory


