




class StringDefence:

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения values для целочисленного типа данных """

        if value == "random":
            if len is None:
                raise ValueError(f"Не объявлена длинна для генерации случайной строки. value={value}")

            if len <= 0:
                raise ValueError(f"Ошибка при генерации случайной строки: Длина строки не может быть меньше или равной 0. value={value}")

            return True


        if type(value) == type([]):
            result = list(map(StringDefence.__string, value))

            if False in result:
                raise ValueError(f"Ошибка при генерации string из списка: Все данные внутри списка должны быть строками\n"
                                 f"Только буквы EN, RU в любом регистре. value={value}")
            return True

        raise ValueError(f"Ошибка при генерации string: Unknow error. value={value}")


    @staticmethod
    def check_value(string):
        return StringDefence.__string(string)



    @staticmethod
    def __string(string) -> bool:
        """Проверяет корректность строки """

        for i in string:
            if i not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
                return False
        return True