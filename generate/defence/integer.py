




class IntegerDefence:

    @staticmethod
    def check_input(value, len: int = 0) -> bool:
        """ Проверяет все возможные значения value для целочисленного типа данных """

        if value == "random":
            return True


        if type(value) == type([]):
            value = list(map(IntegerDefence.__integer, value))

            if False in value:
                raise ValueError(f"Ошибка при генерации integer из списка: Все данные внутри списка должны быть числами. value={value}")

            return True


        if "-" in value:
            start, end = value.split("-")

            if not (IntegerDefence.__integer(start) and IntegerDefence.__integer(end)):
                raise ValueError(f"Ошибка при генерации integer из диапазона: начало и конец диапазона должны быть числами. value={value}")

            if start > end:
                raise ValueError(f"Ошибка при генерации integer из диапазона: начало диапазона не может быть больше конца. value={value}")

            return True

        raise ValueError(f"Ошибка при генерации integer: Unknow error. value={value}")





    @staticmethod
    def check_value(number):
        return IntegerDefence.__integer(number)





    @staticmethod
    def __integer(number) -> bool:
        """Проверяет корректность числа"""

        if type(number) != int and type(number) != str:
            return False

        try:
            number = int(number)
            if number < 0:
                return False
            return True
        except:
            return False