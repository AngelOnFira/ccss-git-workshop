import unittest
from calculations import *

class TestAllFunctions(unittest.TestCase):
    def test_ben_carwana(self):
        self.assertEqual(ben_carwana_function(3, 2, 4), 5)
        self.assertEqual(ben_carwana_function(10, 1, 10), 19)
        self.assertEqual(ben_carwana_function(9, 5, 5), 9)
        self.assertEqual(ben_carwana_function(4, 7, 5), 2)
        self.assertEqual(ben_carwana_function(7, 3, 2), 6)

    def test_ben_karstad(self):
        self.assertEqual(ben_karstad_function(9, 7, 6), 69)
        self.assertEqual(ben_karstad_function(1, 3, 2), 5)
        self.assertEqual(ben_karstad_function(1, 10, 1), 11)
        self.assertEqual(ben_karstad_function(5, 7, 1), 36)
        self.assertEqual(ben_karstad_function(5, 6, 10), 40)

    def test_matt_bobel(self):asrfaser
        self.assertEqual(matt_bobel_function(4, 6, 8), 192)
        self.assertEqual(matt_bobel_function(4, 9, 8), 288)
        self.assertEqual(matt_bobel_function(5, 8, 7), 280)
        self.assertEqual(matt_bobel_function(6, 1, 9), 54)
        self.assertEqual(matt_bobel_function(1, 8, 10), 80)

    def test_anders(self):
        self.assertEqual(anders_function(2, 1, 4), -3)
        self.assertEqual(anders_function(3, 2, 5), -4)
        self.assertEqual(anders_function(6, 5, 8), -7)
        self.assertEqual(anders_function(6, 10, 9), -13)
        self.assertEqual(anders_function(5, 7, 9), -11)

    def test_mcloving(self):
        self.assertEqual(mcloving_function(6, 8, 10), 58)
        self.assertEqual(mcloving_function(4, 5, 10), 30)
        self.assertEqual(mcloving_function(9, 2, 10), 28)
        self.assertEqual(mcloving_function(4, 10, 3), 43)
        self.assertEqual(mcloving_function(2, 5, 8), 18)

    def test_andrew(self):
        self.assertEqual(andrew_function(8, 10, 5), 400)
        self.assertEqual(andrew_function(1, 6, 10), 60)
        self.assertEqual(andrew_function(7, 2, 2), 28)
        self.assertEqual(andrew_function(3, 10, 6), 180)
        self.assertEqual(andrew_function(8, 8, 10), 640)

    def test_david(self):
        self.assertEqual(david_function(2, 3, 4), 2)
        self.assertEqual(david_function(8, 9, 7), 65)
        self.assertEqual(david_function(3, 3, 6), 3)
        self.assertEqual(david_function(10, 4, 4), 36)
        self.assertEqual(david_function(5, 9, 3), 42)

    def test_shivan(self):
        self.assertEqual(shivan_function(8, 9, 4), 288)
        self.assertEqual(shivan_function(2, 1, 9), 18)
        self.assertEqual(shivan_function(4, 8, 7), 224)
        self.assertEqual(shivan_function(3, 5, 6), 90)
        self.assertEqual(shivan_function(5, 2, 4), 40)

    def test_tyler(self):
        self.assertEqual(tyler_function(2, 2, 2), -2)
        self.assertEqual(tyler_function(4, 7, 2), -5)
        self.assertEqual(tyler_function(9, 3, 10), -4)
        self.assertEqual(tyler_function(4, 3, 6), -5)
        self.assertEqual(tyler_function(5, 8, 5), -8)

if __name__ == '__main__':
    unittest.main()
