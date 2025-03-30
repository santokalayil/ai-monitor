# AI Monitor

> ⚠️ **Development Status**: This project is currently in early development and is not ready for production use. The API and functionality may change significantly before the first stable release.

A Python package for monitoring AI systems.

## Installation

You can install the package using UV:

```bash
uv pip install -r requirements.txt
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
2. Install dependencies using UV:
   ```bash
   uv pip install -r requirements.txt
   ```
3. Run `python main.py` to test the package

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is provided "as is" without any warranties, express or implied. The authors and contributors are not responsible for any damages, losses, or issues that may arise from using this software. Users are solely responsible for:

- Verifying the software meets their needs before use
- Testing the software in their specific environment
- Ensuring proper implementation and integration
- Any modifications or customizations they make
- Any issues that arise from their use of the software

By using this software, you agree to take full responsibility for any consequences of its use and to not hold the authors or contributors liable for any problems that may occur.

## Development Status

This project is currently in early development. Please note:

- The API is not stable and may change
- Features are being actively developed
- Documentation is incomplete
- Test coverage is limited
- Not recommended for production use

For more details about the development status and roadmap, see [DEVELOPMENT.md](DEVELOPMENT.md). 