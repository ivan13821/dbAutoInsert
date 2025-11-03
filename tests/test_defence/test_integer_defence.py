import unittest
from generate.defence.integer import IntegerDefence


class TestInteger(unittest.TestCase):

    def test_positive_integer(self):
        """Положительные целые числа"""
        self.assertEqual(IntegerDefence.check_value("123"), True)
        self.assertEqual(IntegerDefence.check_value("0"), True)
        self.assertEqual(IntegerDefence.check_value("999999"), True)

    def test_negative_integer(self):
        """Отрицательные целые числа"""
        self.assertEqual(IntegerDefence.check_value("-123"), False)
        self.assertEqual(IntegerDefence.check_value("-1"), False)
        self.assertEqual(IntegerDefence.check_value("-999999"), False)

    def test_with_whitespace(self):
        """Числа с пробелами"""
        self.assertEqual(IntegerDefence.check_value("  123  "), True)
        self.assertEqual(IntegerDefence.check_value("  -456  "), False)

    def test_incorrected_string(self):
        """Некорректная строка для превращения в число"""
        self.assertEqual(IntegerDefence.check_value(""), False)
        self.assertEqual(IntegerDefence.check_value("123.45"), False)
        self.assertEqual(IntegerDefence.check_value("1e5"), False)
        self.assertEqual(IntegerDefence.check_value("123abc"), False)

    def test_incorrected_type(self):
        """Некорректные типы данных"""
        self.assertEqual(IntegerDefence.check_value([1, 2, 3]), False)
        self.assertEqual(IntegerDefence.check_value(True), False)

        # -----------------------------------

    def test_check_input(self):
        """Входящие в данные из json"""
        self.assertEqual(IntegerDefence.check_input("random"), True, "Should be True")
        self.assertEqual(IntegerDefence.check_input("100-1000"), True, "Should be True")
        self.assertEqual(IntegerDefence.check_input(["100", "1000", "10000"]), True, "Should be True")
        self.assertEqual(IntegerDefence.check_input([100, 1000, 10000]), True, "Should be True")
        self.assertEqual(IntegerDefence.check_input([100, 1000, "10000"]), True, "Should be True")

        with self.assertRaises(ValueError):
            IntegerDefence.check_input(["sss", 100])
        with self.assertRaises(ValueError):
            IntegerDefence.check_input("-100-100")



if __name__ == '__main__':
    unittest.main()