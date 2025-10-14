




class IntegerDefence:

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения value для целочисленного типа данных """
        if value == "random" and len is None:
            raise ValueError("Не объявлена длинна для генерации случайного числа")


        if value == "random" and len <= 0:
            raise ValueError("Ошибка при генерации случайного числа: Длина числа не может быть меньше или равной 0")


        if type(value) == type([]):
            value = list(map(IntegerDefence.__integer, value))

            if False in value:
                raise ValueError("Ошибка при генерации integer из списка: Все данные внутри списка должны быть числами")


        if "-" in value:
            start, end = value.split("-")

            if IntegerDefence.__integer(start) and IntegerDefence.__integer(end):
                pass
            else:
                raise ValueError("Ошибка при генерации integer из диапазона: начало и конец диапазона должны быть числами")

            if start > end:
                raise ValueError("Ошибка при генерации integer из диапазона: начало диапазона не может быть больше конца")

        return True





    @staticmethod
    def check_value(number):
        return IntegerDefence.__integer(number)





    @staticmethod
    def __integer(number) -> bool:
        """Проверяет корректность числа"""

        try:
            int(number)
            return True
        except:
            return False