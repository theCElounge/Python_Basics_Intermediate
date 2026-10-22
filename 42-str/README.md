# Video 42: `__str__`

`print` calls `__str__` to get the text it shows for an object, so `__str__` must return a string, not print it.

| File | What it shows |
|---|---|
| [1_print_an_object.py](1_print_an_object.py) | Printing an object without `__str__` shows its memory address. |
| [2_str_method.py](2_str_method.py) | `__str__` returns the text `print` shows. |
| [3_print_not_return_error.py](3_print_not_return_error.py) | `__str__` that prints instead of returning (TypeError). |

Run a file from this folder:

```
python 1_print_an_object.py
```
