from datetime import datetime

class DateDefence:

    @staticmethod
    def check_input(value, len: str = 0) -> bool:
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

        if type(date) != str:
            return False

        try:
            datetime.strptime(date, "%Y-%m-%d").date()
            return True
        except:
            return False





    @staticmethod
    def __integer(number) -> bool:
        """Проверяет корректность числа"""

        try:
            int(number)
            return True
        except:
            return False