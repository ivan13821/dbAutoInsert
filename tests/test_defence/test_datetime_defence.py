import unittest
from generate.defence.datetime import DateTimeDefence


class TestInteger(unittest.TestCase):

    def test_incorrected_type(self):
        """Типы данных"""
        self.assertEqual(DateTimeDefence.check_value([1, 2, 3]), False)
        self.assertEqual(DateTimeDefence.check_value(True), False)
        self.assertEqual(DateTimeDefence.check_value(100), False)

    def test_string_value(self):
        """Содержимое строки"""
        self.assertEqual(DateTimeDefence.check_value("2020-01-01 10:00:00"), True)
        self.assertEqual(DateTimeDefence.check_value("2020-13-01 10:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01-01 10:60:00"), False)
        self.assertEqual(DateTimeDefence.check_value("100-01-01 10:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01-32 10:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01-01 10:00:60"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01-01 25:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01-01 20:0s:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-0s-01 20:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01-01 20::00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020--01 20:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-0-01 20:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-01 20:00:00"), False)
        self.assertEqual(DateTimeDefence.check_value("2020-00-01 20:00"), False)
        self.assertEqual(DateTimeDefence.check_value(""), False)


    #------------------------------

    def test_check_input(self):
        """Входящие в данные из json"""
        self.assertEqual(DateTimeDefence.check_input("random"), True)
        self.assertEqual(DateTimeDefence.check_input(["2020-01-01 10:00:00", "2021-02-02 12:22:22"]), True)
        self.assertEqual(DateTimeDefence.check_input("2020-01-01|10:00:00 2021-12-28|12:59:59"), True)
        self.assertEqual(DateTimeDefence.check_input("2020-01-01|10:00:00 2020-01-01|12:59:59"), True)

        with self.assertRaises(ValueError):
            DateTimeDefence.check_input(["2020-01-01 :00:00", "2021-02-02 12:22:22"])

        with self.assertRaises(ValueError):
            DateTimeDefence.check_input(["2020-01-01 10:00:00", "2021-02-02 1s:22:22"])

        with self.assertRaises(ValueError):
            DateTimeDefence.check_input(["2020-01-01 10:00:00", "2021-0s-02 11:22:22"])

        with self.assertRaises(ValueError):
            DateTimeDefence.check_input(["2020--01 10:00:00", "2021-02-02 11:22:22"])

        with self.assertRaises(ValueError):
            DateTimeDefence.check_input("2022-01-01|10:00:00 2021-12-28|12:59:59")

        with self.assertRaises(ValueError):
            DateTimeDefence.check_input("2021-01-01|13:00:00 2021-01-01|12:59:59")




if __name__ == '__main__':
    unittest.main()