import unittest
from app import square_pyramidal
class TestPyramidalNumbers(unittest.TestCase):

    def test_basic_values(self):
        self.assertEqual(square_pyramidal(1), 1)
        self.assertEqual(square_pyramidal(2), 5)
        self.assertEqual(square_pyramidal(3), 14)

    def test_calculation(self):
        self.assertEqual(square_pyramidal(10), 385)

    def test_negative_or_zero(self):
        with self.assertRaises(ValueError):
            square_pyramidal(0)

        with self.assertRaises(ValueError):
            square_pyramidal(-5)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            square_pyramidal("3")
        with self.assertRaises(TypeError):
            square_pyramidal(3.5)

if __name__ == '__main__':
    unittest.main(verbosity=2)