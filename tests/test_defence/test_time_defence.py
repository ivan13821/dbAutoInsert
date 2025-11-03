import unittest
from generate.defence.time import TimeDefence


class TestInteger(unittest.TestCase):

    def test_incorrected_type(self):
        """Типы данных"""
        self.assertEqual(TimeDefence.check_value([1, 2, 3]), False)
        self.assertEqual(TimeDefence.check_value(True), False)
        self.assertEqual(TimeDefence.check_value(100), False)

    def test_string_value(self):
        """Содержимое строки"""
        self.assertEqual(TimeDefence.check_value("10:10:10"), True)
        self.assertEqual(TimeDefence.check_value("24:10:10"), False)
        self.assertEqual(TimeDefence.check_value("20:60:10"), False)
        self.assertEqual(TimeDefence.check_value("20:10:60"), False)
        self.assertEqual(TimeDefence.check_value("s0:60:10"), False)
        self.assertEqual(TimeDefence.check_value("20:20"), False)
        self.assertEqual(TimeDefence.check_value(""), False)


    #------------------------------

    def test_check_input(self):
        """Входящие в данные из json"""
        self.assertEqual(TimeDefence.check_input("random"), True)
        self.assertEqual(TimeDefence.check_input(["10:00:00", "12:00:00"]), True)
        self.assertEqual(TimeDefence.check_input("10:00:00 12:59:59"), True)

        with self.assertRaises(ValueError):
            TimeDefence.check_input(["10:00:00", ":00:00"])

        with self.assertRaises(ValueError):
            TimeDefence.check_input(["10:00:00", "11:60:00"])

        with self.assertRaises(ValueError):
            TimeDefence.check_input(["10:00:00", "11:!0:00"])

        with self.assertRaises(ValueError):
            TimeDefence.check_input("10:00:00 9:59:59")




if __name__ == '__main__':
    unittest.main()