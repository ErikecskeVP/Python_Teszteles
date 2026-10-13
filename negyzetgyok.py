import math
import unittest

szam=int(input("Adj meg egy számot: "))

def negyzetgyok(num):
    if num >=0:
        return f'A beírt szám négyzetgyöke {math.sqrt(num)}'
    else:
        return f'Negativ szambol nem vonunk negyzetgyokot!'

negyzetgyok(szam)

class TestNegyzetgyok(unittest.TestCase):
    def test_positive(self):
        ertek=negyzetgyok(1)
        self.assertEqual(ertek, f'A beírt szám négyzetgyöke {math.sqrt(1)}')
    def test_negative(self):
        ertek=negyzetgyok(-1)
        self.assertEqual(ertek, f'Negativ szambol nem vonunk negyzetgyokot!')

unittest.main()