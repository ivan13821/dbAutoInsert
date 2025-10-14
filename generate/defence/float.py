

class FloatDefence:

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения value для целочисленного типа данных """
        if value == "random" and (len is None or number_of_decimal is None):
            raise ValueError("Не объявлено len или number_of_decimal для генерации случайного числа с пл. точкой")

        if value == "random" and (len <= 0 or number_of_decimal <= 0):
            raise ValueError("Ошибка при генерации случайного числа: Длина числа не может быть меньше или равной 0")


        if type(value) == type([]):
            value = list(map(FloatDefence.__float, value))

            if False in value:
                raise ValueError("Ошибка при генерации integer из списка: Все данные внутри списка должны быть числами")


        if "-" in value:
            start, end = value.split("-")

            if FloatDefence.__float(start) and FloatDefence.__float(end):
                pass
            else:
                raise ValueError("Ошибка при генерации integer из диапазона: начало и конец диапазона должны быть числами")

            if start > end:
                raise ValueError("Ошибка при генерации integer из диапазона: начало диапазона не может быть больше конца")

        return True





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