import unittest
from generate.defence.string import StringDefence


class TestInteger(unittest.TestCase):

    def test_incorrected_type(self):
        """Некорректные типы данных"""
        self.assertEqual(StringDefence.check_value([1, 2, 3]), False)
        self.assertEqual(StringDefence.check_value(True), False)
        self.assertEqual(StringDefence.check_value(100), False)

    def test_string_value(self):
        """Некорректное содержимое строки"""
        self.assertEqual(StringDefence.check_value("qwerty"), True)
        self.assertEqual(StringDefence.check_value("qwerty123"), False)
        self.assertEqual(StringDefence.check_value("qwerty@"), False)


    #------------------------------

    def test_check_input(self):
        """Входящие в данные из json"""
        self.assertEqual(StringDefence.check_input("random", 10), True, "Should be True")
        self.assertEqual(StringDefence.check_input(["qwerty", "asd", "i see you"]), True, "Should be True")

        with self.assertRaises(ValueError):
            StringDefence.check_input(["sss", "sss1"])

        with self.assertRaises(ValueError):
            StringDefence.check_input(["sss", "sss@"])

        with self.assertRaises(ValueError):
            StringDefence.check_input(["sss", "sss!"])

        with self.assertRaises(ValueError):
            StringDefence.check_input("random", 0)



if __name__ == '__main__':
    unittest.main()