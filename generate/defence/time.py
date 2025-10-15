
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
                return True

        raise ValueError(f"Ошибка при генерации time: Unknow error. value={value}")





    @staticmethod
    def check_value(time):
        return TimeDefence.__time(time)





    @staticmethod
    def __time(time) -> bool:
        """Проверяет корректность времени"""

        time = time.split(':')

        if len(time) != 3:
            return False

        if False in list(map(TimeDefence.__integer, time)):
            return False

        time = list(map(int, time))
        if not (0 <= time[0] <= 23 and 0 <= time[1] <= 59 and 0 <= time[2] <= 59):
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