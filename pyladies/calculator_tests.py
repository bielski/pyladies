from calculator import Calculator
import unittest


class CalculatorTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 2), 4)


# if __name__ == '__main__':
#     unittest.main()