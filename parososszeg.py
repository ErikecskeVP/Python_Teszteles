import unittest
szam1=int(input("Az intervallum also vegpontja: "))
szam2=int(input("Az intervallum felso vegpontja: "))

def intervallum(n1, n2):
    osszeg=0
    for i in range(n1, n2+1): 
        if i%2==0:
            osszeg+=i
    return f'A(z) [{n1}; {n2}] intervallumba eso paros szamok osszege: {osszeg}'

print(intervallum(szam1, szam2))

class TestParososszeg(unittest.TestCase):
    def test_nulla(self):
        ertek=intervallum(0,0)
        self.assertEqual(ertek, f'A(z) [{0}; {0}] intervallumba eso paros szamok osszege: {0}')

    def test_neg_egy(self):
        ertek=intervallum(-2, 10)
        self.assertLess(ertek, f'A(z) [{-2}; {10}] intervallumba eso paros szamok osszege: {30}')

unittest.main()