import unittest
from division import Division

class TestDivision(unittest.TestCase):
    def test_init(self):
        d=Division(a=1,b=2)
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,2)

    def test_yes(self):
        d=Division(a=8,b=4)        
        self.assertTrue(d.div())

    def test_no(self):
        d=Division(a=10,b=3)
        self.assertFalse(d.div())

if __name__=='__main__':
    unittest.main()