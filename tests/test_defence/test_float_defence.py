import unittest
from generate.defence.float import FloatDefence


class TestInteger(unittest.TestCase):

    def test_incorrected_type(self):
        """Типы данных"""
        self.assertEqual(FloatDefence.check_value([1, 2, 3]), False)
        self.assertEqual(FloatDefence.check_value(True), False)
        self.assertEqual(FloatDefence.check_value(100), False)

    def test_string_value(self):
        """Содержимое строки"""
        self.assertEqual(FloatDefence.check_value("10.11"), True)
        self.assertEqual(FloatDefence.check_value("10,11"), False)
        self.assertEqual(FloatDefence.check_value(".11"), True)
        self.assertEqual(FloatDefence.check_value("111"), True)
        self.assertEqual(FloatDefence.check_value("s1.01"), False)
        self.assertEqual(FloatDefence.check_value("11.0s"), False)
        self.assertEqual(FloatDefence.check_value(""), False)


    #------------------------------

    def test_check_input(self):
        """Входящие в данные из json"""
        self.assertEqual(FloatDefence.check_input("random"), True)
        self.assertEqual(FloatDefence.check_input(["11.11", "22.22"]), True)
        self.assertEqual(FloatDefence.check_input("11.22-22.11"), True)

        with self.assertRaises(ValueError):
            FloatDefence.check_input(["11.11", "22,22"])

        with self.assertRaises(ValueError):
            FloatDefence.check_input("33.22-22.11")

        with self.assertRaises(ValueError):
            FloatDefence.check_input("!3.22-22.11")

        with self.assertRaises(ValueError):
            FloatDefence.check_input("33.22-22.1!")

        with self.assertRaises(ValueError):
            FloatDefence.check_input("33.22-22-11")




if __name__ == '__main__':
    unittest.main()