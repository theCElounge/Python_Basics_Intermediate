# Video 43: Inheritance

A child class like `Dog(Pet)` gets everything from its parent class, and can add its own methods.

| File | What it shows |
|---|---|
| [1_dog_inherits.py](1_dog_inherits.py) | An empty Dog class still has Pet's `__init__` and `__str__`. |
| [2_dog_fetch.py](2_dog_fetch.py) | Dog adds its own `fetch` method. |
| [3_cat_cannot_fetch_error.py](3_cat_cannot_fetch_error.py) | A Cat doesn't get Dog's methods (AttributeError). |

Run a file from this folder:

```
python 1_dog_inherits.py
```
