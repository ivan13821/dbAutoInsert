import unittest
from generate.defence.date import DateDefence

class TestData(unittest.TestCase):

    def test_check_value_day(self):
        """Проверка дней"""
        self.assertEqual(DateDefence.check_value("2020-01-32"), False, "Should be False")
        self.assertEqual(DateDefence.check_value("2023-02-28"), True, "Should be True") #28 февраля в невисокосном году
        self.assertEqual(DateDefence.check_value("2020-02-29"), True, "Should be True") #29 февраля в високосном году
        self.assertEqual(DateDefence.check_value("2023-02-29"), False, "Should be False") #29 февраля в невисокосном году
        self.assertEqual(DateDefence.check_value("2020-02-30"), False, "Should be False") #30 февраля (никогда не валидно)

    def test_check_value_month(self):
        """Проверка месяцов"""
        self.assertEqual(DateDefence.check_value("2020-13-01"), False, "Should be False")
        self.assertEqual(DateDefence.check_value("2020-00-01"), False, "Should be False")
        self.assertEqual(DateDefence.check_value("2020-10-01"), True, "Should be True")

    def test_check_value_year(self):
        """Проверка лет"""
        self.assertEqual(DateDefence.check_value("100-01-01"), False, "Should be False")

    def test_check_value_date(self):
        """Некорректный формат даты"""
        self.assertEqual(DateDefence.check_value("ssss-ss-ss"), False, "Should be False")
        self.assertEqual(DateDefence.check_value("ssss.ss.ss"), False, "Should be False")

    def test_check_value_type(self):
        self.assertEqual(DateDefence.check_value(1), False, "Should be False")
        self.assertEqual(DateDefence.check_value([1, 2, 3]), False, "Should be False")
        self.assertEqual(DateDefence.check_value(True), False, "Should be False")

    #-----------------------------------

    def test_check_input(self):
        """Входящие в данные из json"""
        self.assertEqual(DateDefence.check_input("random"), True, "Should be True")
        self.assertEqual(DateDefence.check_input("2020-12-01 2021-01-01"), True, "Should be True")
        self.assertEqual(DateDefence.check_input(["2019-01-01", "2020-01-01"]), True, "Should be True")

        with self.assertRaises(ValueError):
            DateDefence.check_input(["2019-13-01", "2020-01-01"])
        with self.assertRaises(ValueError):
            DateDefence.check_input("2022-12-01 2021-01-01")


if __name__ == '__main__':
    unittest.main()