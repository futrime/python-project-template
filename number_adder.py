"""Number adder module"""

from typing import List


class NumberAdder:
    """Number adder class"""

    def __init__(self):
        """Initialize the number adder"""

    def add(self, a: int, b: int) -> int:
        """Add two numbers

        Args:
            a: The first number to add.
            b: The second number to add.

        Returns:
            The sum of the two numbers.
        """

        return a + b

    def add_many(self, numbers: List[int]) -> int:
        """Add many numbers

        Args:
            numbers: The list of numbers to add.

        Returns:
            The sum of the numbers.
        """

        return sum(numbers)
