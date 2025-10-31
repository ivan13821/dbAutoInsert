import unittest
from generate.defence.date import DateDefence

class TestSum(unittest.TestCase):

    def test_check_value(self):
        self.assertEqual(DateDefence.check_value("2020-01-01"), True, "Should be True")

if __name__ == '__main__':
    unittest.main()