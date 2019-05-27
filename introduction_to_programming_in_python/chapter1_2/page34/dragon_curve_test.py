import unittest
from dragon_curve import dragon_curve


class DragonCurveTest(unittest.TestCase):
    def test_level_zero(self):
        self.assertEqual(dragon_curve(0), 'F')

    def test_level_one(self):
        self.assertEqual(dragon_curve(1), 'FLF')

    def test_level_two(self):
        self.assertEqual(dragon_curve(2), 'FLFLFRF')

    def test_level_three(self):
        self.assertEqual(dragon_curve(3), 'FLFLFRFLFLFRFRF')


if __name__ == '__main__':
    unittest.main()
