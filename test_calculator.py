"""Automated unit tests for calculator.py."""
import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_subtract_numbers():
    assert subtract(10, 4) == 6

def test_multiply_numbers():
    assert multiply(3, 4) == 12

def test_divide_numbers():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_add_negative_numbers():
    assert add(-2, -3) == -5
