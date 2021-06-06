import unittest
import kalk


class Testkalk(unittest.TestCase):

    def test_add(self):
        self.assertEqual(kalk.add(10, 5), 15)
        self.assertEqual(kalk.add(-1, 1), 0)
        self.assertEqual(kalk.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(kalk.subtract(10, 5), 5)
        self.assertEqual(kalk.subtract(-1, 1), -2)
        self.assertEqual(kalk.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(kalk.multiply(10, 5), 50)
        self.assertEqual(kalk.multiply(-1, 1), -1)
        self.assertEqual(kalk.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(kalk.divide(10, 5), 2)
        self.assertEqual(kalk.divide(-1, 1), -1)
        self.assertEqual(kalk.divide(-1, -1), 1)
        self.assertEqual(kalk.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            kalk.divide(10, 0)


if __name__ == '__main__':
    unittest.main()