import unittest 
from celsius import convert_celsius_to_fahrenheit


class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        temp_celsius = 0
        temp_fahr = convert_celsius_to_fahrenheit(temp_celsius)
        self.assertEqual(32, temp_fahr)


if __name__ == '__main__':
    unittest.main()