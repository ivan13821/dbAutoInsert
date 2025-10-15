

class FloatDefence:

    @staticmethod
    def check_input(value, len) -> bool:
        """ Проверяет все возможные значения value для целочисленного типа данных """

        if value == "random":
            return True


        if type(value) == type([]):
            result = list(map(FloatDefence.__float, value))

            if False in result:
                raise ValueError(f"Ошибка при генерации integer из списка: Все данные внутри списка должны быть числами. value={value}")

            return True


        if "-" in value:
            start, end = value.split("-")

            if FloatDefence.__float(start) and FloatDefence.__float(end):
                pass
            else:
                raise ValueError(f"Ошибка при генерации integer из диапазона: начало и конец диапазона должны быть числами. value={value}")

            if start > end:
                raise ValueError(f"Ошибка при генерации integer из диапазона: начало диапазона не может быть больше конца. value={value}")

            return True

        raise ValueError(f"Ошибка при генерации float: Unknow error. value={value}")





    @staticmethod
    def check_value(number):
        return FloatDefence.__float(number)





    @staticmethod
    def __float(number) -> bool:
        """Проверяет корректность числа"""

        try:
            float(number)
            return True
        except:
            return False