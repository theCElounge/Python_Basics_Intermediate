# Video 39: self and attributes

`self` is the object being built. Saving a value on `self` makes it an attribute, so each object keeps its own data.

| File | What it shows |
|---|---|
| [1_forget_self_error.py](1_forget_self_error.py) | `__init__` without `self` (TypeError). |
| [2_name_not_saved_error.py](2_name_not_saved_error.py) | The name is printed but never saved (AttributeError). |
| [3_save_on_self.py](3_save_on_self.py) | Saving the name and age on `self`, for two pets. |

Run a file from this folder:

```
python 1_forget_self_error.py
```
