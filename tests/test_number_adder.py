"""Test module for the number adder"""

import unittest

from number_adder import NumberAdder


class TestNumberAdder(unittest.TestCase):
    """Test class for the number adder"""

    def setUp(self):
        """Set up the test environment"""

        self._number_adder = NumberAdder()

    def test_add(self):
        """Test the add method"""

        self.assertEqual(self._number_adder.add(1, 2), 3)

    def test_add_many(self):
        """Test the add_many method"""

        self.assertEqual(self._number_adder.add_many([1, 2, 3, 4, 5]), 15)


if __name__ == "__main__":
    unittest.main()
