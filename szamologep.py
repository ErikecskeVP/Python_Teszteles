import unittest

szam1=float(input("Első szám: "))
szam2=float(input("Második szám: "))
muvelet=input("Művelet: ")

def szamologep(num1, num2, mj):
    if mj not in ["+", "-", "*", "/"]:
        return "Hibas muveleti jel!"

    else:
        if mj=="+":
            return f'Az eredmeny: {num1+num2}'
        elif mj=="-":
            return f'Az eredmeny: {num1-num2}'
        elif mj=="*":
            return f'Az eredmeny: {num1*num2}'
        else:
            if num2==0:
                return 'Ejnye, nullaval nem osztunk!'
            else:
                return f'Az eredmeny: {num1/num2}'

print(szamologep(szam1, szam2, muvelet))

class TestSzamologep(unittest.TestCase):
    def test_nulla_osztas(self):
        ertek=szamologep(1,0,"/")
        self.assertEqual(ertek, 'Ejnye, nullaval nem osztunk!')

    def test_negativ_x_negativ(self):
        ertek=szamologep(-5, -6, "*")
        self.assertGreater(ertek, f'Az eredmeny: {0}')

    def test_hibas_jel(self):
        ertek=szamologep(1,2,"!")
        self.assertEqual(ertek, "Hibas muveleti jel!")

    def test_poz_bol_neg(self):
        ertek=szamologep(1202, (-21), "-")
        self.assertEqual(ertek, f'Az eredmeny: {1202+abs(-21)}')

    def test_poz_x_negativ(self):
        ertek=szamologep(121312, -21211, "*")
        self.assertLess(ertek, f'Az eredmeny: {0}')

    

unittest.main()