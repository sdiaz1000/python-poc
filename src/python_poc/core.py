"""Core functionality for the Python POC project."""

from typing import Callable, Dict, Union


def greet(name: str) -> str:
    """
    Generate a greeting message for the given name.

    Args:
        name: The name to greet

    Returns:
        A greeting message

    Example:
        >>> greet("World")
        'Hello, World!'
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not name.strip():
        raise ValueError("Name cannot be empty")

    return f"Hello, {name.strip()}!"


def calculate(
    a: Union[int, float], b: Union[int, float], operation: str = "add"
) -> Union[int, float]:
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        a: First number
        b: Second number
        operation: Operation to perform ('add', 'subtract', 'multiply',
                               'divide')

    Returns:
        Result of the arithmetic operation

    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If dividing by zero

    Example:
        >>> calculate(2, 3, "add")
        5
        >>> calculate(10, 2, "divide")
        5.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    def _divide(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    operations: Dict[
        str, Callable[[Union[int, float], Union[int, float]], Union[int, float]]
    ] = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": _divide,
    }

    if operation not in operations:
        raise ValueError(
            f"Unsupported operation: {operation}. "
            f"Choose from: {', '.join(operations.keys())}"
        )

    return operations[operation](a, b)
