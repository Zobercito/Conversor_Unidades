import unittest

from units import convertir_distancia, convertir_temperatura


class TestUnits(unittest.TestCase):
    def test_distancia(self):
        # 1 km = 1000 m
        self.assertAlmostEqual(convertir_distancia(1, 'km', 'm'), 1000)
        # 1 mi = 1.609344 km
        self.assertAlmostEqual(convertir_distancia(1, 'mi', 'km'), 1.609344, places=6)

    def test_temperatura(self):
        # Celsius <-> Fahrenheit
        self.assertAlmostEqual(convertir_temperatura(0, 'C', 'F'), 32)
        self.assertAlmostEqual(convertir_temperatura(32, 'F', 'C'), 0)
        # Celsius -> Kelvin
        self.assertAlmostEqual(convertir_temperatura(0, 'C', 'K'), 273.15)


if __name__ == '__main__':
    unittest.main()
