import unittest
from app import square_pyramidal
class TestPyramidalNumbers(unittest.TestCase):

    def test_basic_values(self):
        self.assertEqual(square_pyramidal(1), 1)
        self.assertEqual(square_pyramidal(2), 5)
        self.assertEqual(square_pyramidal(10), 385)

    def test_negative_or_zero(self):
        expected_message = "Число n має бути натуральним (більше 0)."
        self.assertEqual(square_pyramidal(0), expected_message)
        self.assertEqual(square_pyramidal(-5), expected_message)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            square_pyramidal("текст")

if __name__ == '__main__':
    unittest.main()