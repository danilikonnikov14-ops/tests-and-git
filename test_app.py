import unittest
from main import add, divide

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_divide(self):
        self.assertEqual(divide(10, 1), 10)
        self.assertEqual(divide(90, 9), 10)
        self.assertEqual(divide(11, 11), 1)
        self.assertEqual(divide(10, 1), 10)
        self.assertEqual(divide(55, 5), 11)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(11, 11), 1)
        self.assertEqual(divide(100, 10), 10)
        self.assertEqual(divide(1, 1), 1)
        

if __name__ == '__main__':
    unittest.main()