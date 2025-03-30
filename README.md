# AI Monitor

A Python package for monitoring AI systems.

## Installation

You can install the package using Poetry:

```bash
poetry install
```

Or using pip:

```bash
pip install -e .
```

## Usage

```python
from ai.core import monitor_status, get_version

# Get the current version
version = get_version()
print(f"AI Monitor Version: {version}")

# Check AI system status
status = monitor_status()
print(f"Status: {status}")
```

## Development

To set up the development environment:

1. Clone the repository
2. Install Poetry if you haven't already
3. Run `poetry install`
4. Run `poetry shell` to activate the virtual environment
5. Run `python main.py` to test the package

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 