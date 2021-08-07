import unittest
from calc import calc

class myTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = calc(4,2)

    def setUp(self):
        self.calc.set_values(4,2)

    def test_add(self):
        #cal = calc(4,2)
        self.assertEqual(self.calc.add(),6)

    def test_mul(self):
        #cal = calc(4,2)
        self.assertEqual(self.calc.mul(),8)

    def test_div(self):
        #cal = calc(4,2)
        self.assertEqual(self.calc.div(),2)

unittest.main(verbosity=2)