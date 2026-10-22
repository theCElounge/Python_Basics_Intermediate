# Video 41: Changing an object

We change an attribute with a dot: from outside with `pet1.age = 4`, or inside a method with `self.age`.

| File | What it shows |
|---|---|
| [1_change_with_a_dot.py](1_change_with_a_dot.py) | Changing one pet's age changes only that pet. |
| [2_birthday_error.py](2_birthday_error.py) | A method that uses `age` instead of `self.age` (UnboundLocalError). |
| [3_birthday_fixed.py](3_birthday_fixed.py) | The `birthday` method with `self.age += 1`. |

Run a file from this folder:

```
python 1_change_with_a_dot.py
```
