def add(a, b):
    """Return sum of two numbers."""
    return a + b


def divide(a, b):
    """Return division of a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
