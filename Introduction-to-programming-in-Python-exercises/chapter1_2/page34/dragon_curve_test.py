import unittest
from dragon_curve import dragonCurve

class DragonCurveTest(unittest.TestCase):
    def test_level_zero(self):
        self.assertEqual(dragonCurve(0),'F')
    def test_level_one(self):
        self.assertEqual(dragonCurve(1),'FLF')
    def test_level_two(self):
        self.assertEqual(dragonCurve(2),'FLFLFRF')
    def test_level_three(self):
        self.assertEqual(dragonCurve(3),'FLFLFRFLFLFRFRF')

if __name__ == '__main__':
    unittest.main()