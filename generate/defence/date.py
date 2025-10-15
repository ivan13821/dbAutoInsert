from datetime import datetime

class DateDefence:

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения value для целочисленного типа данных """

        if value == "random":
            return True


        if type(value) == type([]):
            value = list(map(DateDefence.__date, value))

            if False in value:
                raise ValueError(f"Ошибка при генерации integer из списка: Некорректная дата в списке. value={value}")

            return True


        if " " in value:
            start, end = value.split(" ")

            if not (DateDefence.__date(start) and DateDefence.__date(end)):
                raise ValueError(f"Ошибка при генерации date из диапазона: начало и конец диапазона должны быть датами. value={value}")


            if datetime.strptime(start, '%Y-%m-%d') > datetime.strptime(end, '%Y-%m-%d'):
                raise ValueError(f"Ошибка при генерации date из диапазона: начало диапазона не может быть больше конца. value={value}")

            return True

        raise ValueError(f"Ошибка при генерации date: Unknow error. value={value}")





    @staticmethod
    def check_value(number):
        return DateDefence.__date(number)





    @staticmethod
    def __date(date, split="-") -> bool:
        """Проверяет корректность даты"""

        day_on_month = {
            1:31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        date = date.split(split)

        if False in list(map(DateDefence.__integer, date)): return False

        year, month, day = date

        if not (len(month) == 2 and len(day) == 2):
            return False

        if not (1970 <= int(year) and 1 <= int(month) <= 12 and 1 <= int(day) <= day_on_month[int(month)]):
            return False

        return True





    @staticmethod
    def __integer(number) -> bool:
        """Проверяет корректность числа"""

        try:
            int(number)
            return True
        except:
            return False