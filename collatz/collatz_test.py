import unittest

from collatz import collatz

class collatz_test(unittest.TestCase):
  def test_one(self):
    self.assertEqual(collatz(1), 0)
  
  def test_27(self):
    self.assertEqual(collatz(27), 111)

if __name__ == '__main__':
  unittest.main()