import unittest
import os
import sys

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, SRC_DIR)

from Project import Converter

class Test(unittest.TestCase):

    #Тестируем возращаемое число 1000 где X >= 100.7
    def test_1007(self):
        x = 100.7
        res = Converter.do(x)
        self.assertEqual(1000, res)

    def test_1007_1(self):
        x = 100.8
        res = Converter.do(x)
        self.assertEqual(1000, res)

    def test_1007_2(self):
        x = 100.9
        res = Converter.do(x)
        self.assertEqual(1000, res)

    def test_1007_3(self):
        x = 10000
        res = Converter.do(x)
        self.assertEqual(1000, res)

    def test_1007_4(self):
        x = 1000
        res = Converter.do(x)
        self.assertEqual(1000, res)


    #Тестируем возращаемое число эквивалентно int(x)

    def test_x(self):
        x = 100.6
        res = Converter.do(x)
        self.assertEqual(int(x), res)

    def test_x_1(self):
        x = 100
        res = Converter.do(x)
        self.assertEqual(int(x), res)

    def test_x_2(self):
        x = 50
        res = Converter.do(x)
        self.assertEqual(int(x), res)

    def test_x_3(self):
        x = 1
        res = Converter.do(x)
        self.assertEqual(int(x), res)

    def test_x_4(self):
        x = 0.1
        res = Converter.do(x)
        self.assertEqual(int(x), res)

    #тестируем возращаемое значение где x >= -30.4

    def test_304(self):
        x = -30.4
        res = Converter.do(x)
        self.assertEqual(int(x)-5, res)

    def test_304_2(self):
        x = -20
        res = Converter.do(x)
        self.assertEqual(int(x)-5, res)

    #тестируем генерацию исключения ValueError
    def test_x0(self):
        x = 0
        with self.assertRaises(ValueError):
            Converter.do(x)














if __name__ == "__main__":
    unittest.main()