import unittest 

def convert_celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32 


class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        temp_celsius = 0
        temp_fahr = convert_celsius_to_fahrenheit(temp_celsius)
        self.assertEqual(32, temp_fahr)


if __name__ == '__main__':
    unittest.main()