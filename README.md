# IDManager

`IDManager` is a Python class designed to manage sequential IDs. It allows you to initialize a starting ID and a step size, retrieve the next available ID, and reset the ID sequence.

## Features

- **Configurable Start and Step**: Initialize the ID sequence with a custom starting value and increment step.
- **Sequential ID Generation**: Easily retrieve the next ID in the sequence.
- **Reset Functionality**: Reset the ID sequence to a specified starting value.

## Installation

You can install this package directly from GitHub:

```bash
pip install git+[https://github.com/ry-yoshida-private/IDManager.git](https://github.com/ry-yoshida-private/IDManager.git)
```

## Usage

```python
from manager import IDManager

# Initialize IDManager with default values (start=0, step=1)
manager = IDManager()
print(f"Next ID: {manager.get_next_id()}")  # Output: Next ID: 0
print(f"Next ID: {manager.get_next_id()}")  # Output: Next ID: 1

# Initialize with custom start and step
custom_manager = IDManager(start=10, step=5)
print(f"Next ID: {custom_manager.get_next_id()}")  # Output: Next ID: 10
print(f"Next ID: {custom_manager.get_next_id()}")  # Output: Next ID: 15

# Reset the manager
manager.reset(start=100)
print(f"Next ID after reset: {manager.get_next_id()}") # Output: Next ID after reset: 100
```

## License

TThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Acknowledgments
This package includes code derived from UniversalTracker, developed by RIIPS (Research Institute for Infrastructure Paradigm Shift), an in-house laboratory of Yachiyo Engineering Co., Ltd.