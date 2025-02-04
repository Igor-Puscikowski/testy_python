import unittest
from bank import Bank

class TestBank(unittest.TestCase):
    def test_initial_balance(self):
        acc1 = Bank("Igor","Puscik",20302)
        self.assertEqual(acc1.balance,0)

    def test_pesel_10(self):
        acc2 = Bank("kuba","kowal",1234567890)
        self.assertEqual(acc2.pesel,"pesel niepoprawny")

    def test_pesel_12(self):
        acc2 = Bank("kuba", "kowal", 123456789012)
        self.assertEqual(acc2.pesel, "pesel niepoprawny")

    # ten powinien byc faild co oznacz ze jest gitara pesel
    def test_pesel_11(self):
        acc2 = Bank("kuba", "kowal", 12345678901)
        self.assertEqual(acc2.pesel, "pesel poprawny")

    def test_age_birth_after_60(self):
        acc5 = Bank("kuba", "kowal", 65345678901, bonus="PROM_XY3Z9")
        self.assertEqual(acc5.balance, 50)
    def test_age_birth_before_60(self):
        acc5 = Bank("kuba", "kowal", 55345678901, bonus="PROM_XY3Z9")
        self.assertEqual(acc5.balance, 50)
        """za stary"""



if __name__ == '__main__':
    unittest.main()
