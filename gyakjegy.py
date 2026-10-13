import unittest

pontszam=int(input("A pontszámod: "))

def gyakjegy(szam):
    if 0<=szam<=100:
        if 85<=szam<=100:
            return f'Az érdemjegyed: Jeles (5)'
        elif 70<=szam<=84:
            return  f'Az érdemjegyed: Jó (4)'
        elif 55<=szam<=69:
                    return  f'Az érdemjegyed: Közepes (3)'
        elif 40<=szam<=54:
                    return  f'Az érdemjegyed: Elégséges (2)'
        else:
               return f'Az érdemjegyed: Elégtelen (1)'

    else:
         return f'Érvénytelen érték!'
print(gyakjegy(pontszam))

class TestGyakjegyFunction(unittest.TestCase):
    def test_otos(self):
        ertek=gyakjegy(85)
        self.assertEqual(ertek, 'Az érdemjegyed: Jeles (5)')

    def test_negyes(self):
        ertek=gyakjegy(82)
        self.assertEqual(ertek, 'Az érdemjegyed: Jó (4)')

    def test_harmas(self):
        ertek=gyakjegy(69)
        self.assertEqual(ertek, 'Az érdemjegyed: Közepes (3)')

    def test_negyes(self):
        ertek=gyakjegy(45)
        self.assertEqual(ertek, 'Az érdemjegyed: Megfelelt (2)')

    def test_negyes(self):
        ertek=gyakjegy(13)
        self.assertEqual(ertek, 'Az érdemjegyed: Elégtelen (1)')

    def test_rossz(self):
        ertek=gyakjegy(-1)
        self.assertEqual(ertek, 'Érvénytelen érték!')

unittest.main()

        