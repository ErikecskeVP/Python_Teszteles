import unittest

def sajat_abs(num:int):
    return num*-1

class TestAbsFunction(unittest.TestCase):
    def test_one_positive(self):
        ertek=sajat_abs(10)
        self.assertGreater(ertek, 0)

    def test_one_negative(self):
        ertek=sajat_abs(-13)
        self.assertGreater(ertek, 0)

    def test_zero(self):
        ertek=sajat_abs(0)
        self.assertEqual(ertek, 0)

unittest.main()
