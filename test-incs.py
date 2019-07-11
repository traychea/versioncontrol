from incs import * 
import unittest

class KnownIncs(unittest.TestCase):

    def test_iszero(self):
        self.assertEqual(is_zero(1), False)
        self.assertEqual(is_zero(0), True)

    def test_isone(self): 
        self.assertEqual(is_one(1), True)
        self.assertEqual(is_one(0), False)

    def test_inc1(self):
        self.assertEqual(inc1(0), 1)
        self.assertEqual(inc1(1000), 1001)

    def test_inc2(self):
        self.assertEqual(inc2(0), 2)
        self.assertEqual(inc2(1000), 1002)

    def test_inc3(self):
        self.assertEqual(inc3(0), 3)
        self.assertEqual(inc3(1000), 1003)

    def test_inc4(self):
        self.assertEqual(inc4(0), 4)
        self.assertEqual(inc4(1000), 1004)

    def test_inc5(self):
        self.assertEqual(inc5(0), 5)
        self.assertEqual(inc5(1000), 1005)

    def test_inc6(self):
        self.assertEqual(inc6(0), "6")
        self.assertEqual(inc6(1000), "1006")

    def test_inc7(self):
        self.assertEqual(inc7(0), "7")
        self.assertEqual(inc7(1000), "1007")


if __name__ == "__main__":
    unittest.main()

