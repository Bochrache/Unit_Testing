# Python Unit Testing with pytest and Nix

This project demonstrates how to set up a reproducible Python testing environment using pytest and Nix. It includes comprehensive examples of testing best practices for Python functions.

## 📋 Prerequisites

Before you begin, make sure you have the following installed:
- [Nix package manager](https://nixos.org/download.html)
- Git
- A text editor (VS Code recommended)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Bochrache/Unit_Testing.git
cd Unit_Testing
```

### 2. Enter the Nix Environment

The project uses Nix for reproducible development environments. Enter the environment with:

```bash
nix-shell
```

This will automatically set up Python 3.13 with all required dependencies:
- numpy
- pytest
- pytest-cov (for coverage reports)
- black (code formatter)
- flake8 (linter)

### 3. Verify the Setup

Once in the Nix shell, verify everything is working:

```bash
# Check Python version
python --version

# Run all tests
pytest

# Run tests with verbose output
pytest -v
```

## 📁 Project Structure

```
Unit_Testing/
├── shell.nix                          # Nix environment configuration
├── utils.py                           # Main function to test
├── tests/
│   ├── __init__.py                    # Makes tests a Python package
│   ├── test_utils.py                  # Basic pytest examples
│   └── test_utils_comprehensive.py    # Advanced testing patterns
├── .gitignore                         # Git ignore file
└── README.md                          # This file
```

## 🧪 Running Tests

### Basic Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_utils.py

# Run tests with coverage report
pytest --cov=utils

# Run tests with HTML coverage report
pytest --cov=utils --cov-report=html
```

### Test Categories

1. **Basic Tests** (`test_utils.py`):
   - Simple function testing
   - NaN value handling
   - Floating-point comparisons

2. **Comprehensive Tests** (`test_utils_comprehensive.py`):
   - Edge cases (empty arrays, single values)
   - Parametrized tests
   - Class-based test organization
   - Error handling

## 📝 Understanding the Code

### Main Function (`utils.py`)

```python
def normalize_vector(x):
    """Normalize a vector using z-score normalization."""
    return (x - np.nanmean(x)) / np.nanstd(x)
```

### Key Testing Concepts Demonstrated

1. **Setup-Action-Expectation Pattern**:
   ```python
   def test_normalize_vector_basic():
       # 1. Setup
       input_vector = np.array([10, 20, 30])
       expected_output = np.array([-1.22474487, 0.0, 1.22474487])
       
       # 2. Action
       actual_output = normalize_vector(input_vector)
       
       # 3. Expectation
       assert np.allclose(actual_output, expected_output)
   ```

2. **Floating-Point Comparisons**:
   - Use `np.allclose()` for floating-point comparisons
   - Use `np.testing.assert_allclose()` for NaN handling

3. **Parametrized Testing**:
   ```python
   @pytest.mark.parametrize("input_data,expected", [
       (np.array([1, 2, 3]), np.array([-1.22474487, 0.0, 1.22474487])),
       (np.array([0, 0, 0]), np.array([np.nan, np.nan, np.nan])),
   ])
   def test_normalize_vector_parametrized(input_data, expected):
       # Test implementation
   ```

4. **Exception Testing**:
   ```python
   def test_function_raises_exception():
       with pytest.raises(ValueError):
           some_function_that_should_fail()
   ```

## 🛠 Development Workflow

### Adding New Tests

1. Create test functions starting with `test_`
2. Use descriptive names: `test_function_name_scenario`
3. Follow the Setup-Action-Expectation pattern
4. Run tests frequently during development

### Code Quality

```bash
# Format code with black
black utils.py tests/

# Check code style with flake8
flake8 utils.py tests/

# Run tests with coverage
pytest --cov=utils --cov-report=term-missing
```

### Git Workflow

```bash
# Make changes
# ...

# Add and commit
git add .
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

## 🔧 Customizing the Environment

### Modifying Dependencies

Edit `shell.nix` to add or remove Python packages:

```nix
buildInputs = with pkgs; [
  python3
  python3Packages.numpy
  python3Packages.pytest
  python3Packages.your-new-package  # Add new packages here
];
```

### Adding New Test Files

1. Create files in the `tests/` directory starting with `test_`
2. Import the functions you want to test
3. Write test functions starting with `test_`

## 📚 pytest Best Practices

1. **Test Naming**: Use descriptive names that explain what you're testing
2. **Test Organization**: Group related tests in classes or separate files
3. **Assertions**: Use appropriate assertion methods for your data types
4. **Edge Cases**: Always test boundary conditions and error cases
5. **Documentation**: Add docstrings to complex test functions

## 🔍 Troubleshooting

### Common Issues

1. **Nix not found**: Install Nix package manager
2. **Tests failing**: Check that you're in the nix-shell environment
3. **Import errors**: Ensure you're running tests from the project root
4. **Cache issues**: Delete `__pycache__` directories and `.pytest_cache`

### Getting Help

- Run `pytest --help` for pytest options
- Check the [pytest documentation](https://docs.pytest.org/)
- Review the [NumPy testing guidelines](https://numpy.org/doc/stable/reference/routines.testing.html)

## 🎯 Next Steps

1. Add more functions to `utils.py`
2. Create corresponding tests
3. Experiment with fixtures and test data
4. Try pytest plugins (pytest-benchmark, pytest-mock, etc.)
5. Set up continuous integration with GitHub Actions

## 📄 License

This project is for educational purposes as part of WP2 coursework.