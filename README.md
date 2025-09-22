# Python POC

[![CI](https://github.com/sdiaz1000/python-poc/workflows/CI/badge.svg)](https://github.com/sdiaz1000/python-poc/actions)
[![codecov](https://codecov.io/gh/sdiaz1000/python-poc/branch/main/graph/badge.svg)](https://codecov.io/gh/sdiaz1000/python-poc)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python proof of concept project demonstrating best practices for Python package development.

## Features

- 🏗️ Modern Python project structure with `pyproject.toml`
- 🧪 Comprehensive testing with pytest and coverage reporting
- 🔧 Code formatting with Black and import sorting with isort
- 🚨 Linting with flake8 and type checking with mypy
- 🔄 Pre-commit hooks for code quality
- 🚀 GitHub Actions CI/CD pipeline
- 📦 Automated package building and publishing setup

## Installation

### For Users

```bash
pip install python-poc
```

### For Development

```bash
# Clone the repository
git clone https://github.com/sdiaz1000/python-poc.git
cd python-poc

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Usage

```python
from python_poc import greet, calculate

# Basic greeting
message = greet("World")
print(message)  # Output: Hello, World!

# Basic arithmetic
result = calculate(10, 5, "add")
print(result)  # Output: 15

result = calculate(10, 2, "divide")
print(result)  # Output: 5.0
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=python_poc

# Run tests with detailed coverage report
pytest --cov=python_poc --cov-report=html
```

### Code Quality

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Lint code
flake8 src

# Type checking
mypy src

# Run all quality checks
pre-commit run --all-files
```

### Building

```bash
# Build the package
python -m build

# Install the built package
pip install dist/python_poc-*.whl
```

## Project Structure

```
python-poc/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── src/
│   └── python_poc/
│       ├── __init__.py         # Package initialization
│       └── core.py             # Core functionality
├── tests/
│   ├── __init__.py
│   └── test_core.py            # Test cases
├── .gitignore                  # Git ignore rules
├── .pre-commit-config.yaml     # Pre-commit configuration
├── pyproject.toml              # Project configuration
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
└── README.md                   # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the test suite (`pytest`)
5. Run code quality checks (`pre-commit run --all-files`)
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### [0.1.0] - 2024-01-01

#### Added
- Initial project setup with modern Python tooling
- Basic greeting and calculation functionality
- Comprehensive test suite
- CI/CD pipeline with GitHub Actions
- Code quality tools and pre-commit hooks