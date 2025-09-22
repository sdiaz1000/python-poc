"""Tests for the core module."""

import pytest

from python_poc.core import calculate, greet


class TestGreet:
    """Test cases for the greet function."""

    def test_greet_valid_name(self):
        """Test greeting with a valid name."""
        result = greet("World")
        assert result == "Hello, World!"

    def test_greet_with_spaces(self):
        """Test greeting with a name that has leading/trailing spaces."""
        result = greet("  Alice  ")
        assert result == "Hello, Alice!"

    def test_greet_empty_string(self):
        """Test greeting with an empty string raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    def test_greet_whitespace_only(self):
        """Test greeting with whitespace-only string raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("   ")

    def test_greet_non_string(self):
        """Test greeting with non-string input raises TypeError."""
        with pytest.raises(TypeError, match="Name must be a string"):
            greet(123)


class TestCalculate:
    """Test cases for the calculate function."""

    def test_add_integers(self):
        """Test addition with integers."""
        result = calculate(2, 3, "add")
        assert result == 5

    def test_add_floats(self):
        """Test addition with floats."""
        result = calculate(2.5, 3.7, "add")
        assert result == pytest.approx(6.2)

    def test_subtract(self):
        """Test subtraction."""
        result = calculate(10, 3, "subtract")
        assert result == 7

    def test_multiply(self):
        """Test multiplication."""
        result = calculate(4, 5, "multiply")
        assert result == 20

    def test_divide(self):
        """Test division."""
        result = calculate(10, 2, "divide")
        assert result == 5.0

    def test_divide_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calculate(10, 0, "divide")

    def test_invalid_operation(self):
        """Test invalid operation raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported operation: power"):
            calculate(2, 3, "power")

    def test_non_numeric_input(self):
        """Test non-numeric input raises TypeError."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            calculate("2", 3, "add")

    def test_default_operation(self):
        """Test default operation is addition."""
        result = calculate(2, 3)
        assert result == 5

    @pytest.mark.parametrize(
        "a,b,op,expected",
        [
            (1, 1, "add", 2),
            (5, 3, "subtract", 2),
            (3, 4, "multiply", 12),
            (8, 2, "divide", 4.0),
            (-1, 1, "add", 0),
            (0, 5, "multiply", 0),
        ],
    )
    def test_calculate_parametrized(self, a, b, op, expected):
        """Test calculate function with various parameter combinations."""
        result = calculate(a, b, op)
        assert result == expected
