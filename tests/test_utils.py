"""Tests for py14days.utils module."""

import pytest

from py14days.utils import add, divide, factorial, is_palindrome, multiply, subtract


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_add_zero(self):
        assert add(0, 7) == 7

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_to_negative(self):
        assert subtract(3, 8) == -5

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(99, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_results_in_float(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_non_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") is True

    def test_palindrome_mixed_case(self):
        assert is_palindrome("RaceCar") is True

    def test_single_character(self):
        assert is_palindrome("a") is True

    def test_empty_string(self):
        assert is_palindrome("") is True


class TestFactorial:
    def test_factorial_of_zero(self):
        assert factorial(0) == 1

    def test_factorial_of_one(self):
        assert factorial(1) == 1

    def test_factorial_of_five(self):
        assert factorial(5) == 120

    def test_factorial_of_ten(self):
        assert factorial(10) == 3628800

    def test_factorial_negative_raises(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-1)
