# Contributing to AI Monitor

Thank you for your interest in contributing to AI Monitor! This document provides guidelines and information for contributors.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure everything works
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone your fork of the repository
2. Install Poetry if you haven't already
3. Run `poetry install`
4. Run `poetry shell` to activate the virtual environment
5. Make your changes
6. Run tests before submitting a PR

## Code Style

- Follow PEP 8 guidelines
- Use type hints for all function parameters and return values
- Add docstrings for all public functions and classes
- Keep functions focused and single-purpose

## Testing

- Add tests for new features
- Ensure all tests pass before submitting PR
- Maintain or improve test coverage

## Documentation

- Update README.md if needed
- Add docstrings to new functions/classes
- Update any relevant documentation

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the version number in `ai/ai/version.py` following semantic versioning
3. The PR will be merged once you have the sign-off of at least one maintainer

## Release Process

1. Update version numbers in:
   - `ai/ai/version.py`
   - `pyproject.toml`
2. Create a new release on GitHub
3. Tag the release with the version number

## Disclaimer for Contributors

By contributing to this project, you agree that:

1. Your contributions are provided "as is" without any warranties
2. You are not liable for any issues that may arise from your contributions
3. You have the right to contribute the code you submit
4. Your contributions do not violate any third-party rights
5. You understand that your contributions may be modified or removed at any time
6. You will not hold the project maintainers liable for any issues arising from your contributions

## Questions?

If you have any questions, please open an issue in the GitHub repository. 