import unittest
from bank import Bank

class TestBank(unittest.TestCase):
    def test_initial_balance(self):
        acc1 = Bank("Igor","Puscik")
        self.assertEqual(acc1.balance,0)
if __name__ == '__main__':
    unittest.main()
