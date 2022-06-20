import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Test the city_country() function in city_functions.py"""

    def test_city_country(self):
        """Will a location like 'Santiago, Chile' work?"""
        final_name = city_country("santiago", "chile")
        self.assertEqual(final_name, "Santiago, Chile")

    def test_city_country_population(self):
        """
        Will a statement like 'Santiago, Chile - population 5000000' work
        """
        final_name = city_country("santiago", "chile", population=5_000_000)
        self.assertEqual(final_name, "Santiago, Chile - population 5000000")


if __name__ == "__main__":
    unittest.main()
