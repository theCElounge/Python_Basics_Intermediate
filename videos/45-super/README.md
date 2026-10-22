# Video 45: `super()`

`super()` lets a child class run its parent's version of a method, and then add its own code.

| File | What it shows |
|---|---|
| [1_without_super_error.py](1_without_super_error.py) | Dog's own `__init__` skips Pet's, so the name is never saved (AttributeError). |
| [2_with_super.py](2_with_super.py) | `super().__init__(name, age)` runs Pet's `__init__` first. |

Run a file from this folder:

```
python 1_without_super_error.py
```
