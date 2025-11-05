import unittest
from generate.defence.datetime import DateTimeDefence
from generate.defence.date import DateDefence
from generate.defence.time import TimeDefence
from generate.defence.integer import IntegerDefence
from generate.defence.string import StringDefence
from generate.defence.float import FloatDefence
from generate.main import Generate




class TestInteger(unittest.TestCase):


    def test_generate_string(self):
        """Генерация строки"""

        for i in range(10000):
            self.assertEqual(StringDefence.check_value(Generate.string("random", 10)), True)
            self.assertEqual(StringDefence.check_value(Generate.string(["Anna", "Bob", "Tom"])), True)


    def test_generate_integer(self):
        """Генерация целого числа"""

        for i in range(10000):
            self.assertEqual(IntegerDefence.check_value(Generate.integer("random")), True)
            self.assertEqual(IntegerDefence.check_value(Generate.integer(["10", "111", "1222"])), True)
            self.assertEqual(IntegerDefence.check_value(Generate.integer("1-10000")), True)


    def test_generate_float(self):
        """Генерация числа с плавающей точкой"""

        for i in range(10000):
            self.assertEqual(FloatDefence.check_value(Generate.float("random")), True)
            self.assertEqual(FloatDefence.check_value(Generate.float(["10.10", "111.111", "1222.1222"])), True)
            self.assertEqual(FloatDefence.check_value(Generate.float("1-10000")), True)


    def test_generate_time(self):
        """Генерация времени"""

        for i in range(10000):
            self.assertEqual(TimeDefence.check_value(Generate.time("random")), True)
            self.assertEqual(TimeDefence.check_value(Generate.time(["10:00:00", "10:10:00", "10:10:10"])), True)
            self.assertEqual(TimeDefence.check_value(Generate.time("10:00:00 20:00:00")), True)


    def test_generate_date(self):
        """Генерация даты"""

        for i in range(10000):
            self.assertEqual(DateDefence.check_value(Generate.date("random")), True)
            self.assertEqual(DateDefence.check_value(Generate.date(["2021-01-01", "2021-10-01", "2021-01-10"])), True)
            self.assertEqual(DateDefence.check_value(Generate.date("2021-01-01 2025-01-01")), True)


    def test_generate_datetime(self):
        """Генерация даты и времени"""

        for i in range(10000):
            self.assertEqual(DateTimeDefence.check_value(Generate.datetime("random")), True)
            self.assertEqual(DateTimeDefence.check_value(Generate.datetime(["2021-01-25 10:10:10", "2021-10-01 10:00:00", "2021-10-10 10:00:10"])), True)
            self.assertEqual(DateTimeDefence.check_value(Generate.datetime("2021-01-01|00:00:00 2025-01-01|00:00:00")), True)