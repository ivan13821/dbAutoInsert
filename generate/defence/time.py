from datetime import time


class TimeDefence:

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения value для целочисленного типа данных """

        if value == "random":
            return True


        if type(value) == type([]):
            result = list(map(TimeDefence.__time, value))

            if False in result:
                raise ValueError(f"Ошибка при генерации time из списка: Некорректное время в списке:{value}")
            else:
                return True


        if " " in value:
            start, end = value.split(" ")

            if TimeDefence.__time(start) == False or TimeDefence.__time(end) == False:
                raise ValueError(f"Ошибка при генерации time из диапазона: Некорректное время в внури диапазона: {value}")
            else:
                h, m, s = map(int, start.split(':'))
                start = time(h, m, s)
                h, m, s = map(int, end.split(':'))
                end = time(h, m, s)
                if start >= end:
                    raise ValueError(
                        f"Ошибка при генерации time из диапазона: начало диапазона не может быть больше конца: {value}")
                return True

        raise ValueError(f"Ошибка при генерации time: Unknow error. value={value}")





    @staticmethod
    def check_value(time):
        return TimeDefence.__time(time)





    @staticmethod
    def __time(input_time) -> bool:
        """Проверяет корректность времени"""

        if type(input_time) != str:
            return False

        try:
            h, m, s = map(int, input_time.split(':'))
            time(h, m, s)
            return True
        except:
            return False
