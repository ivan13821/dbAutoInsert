




class StringDefence:

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения values для целочисленного типа данных """

        if value == "random" and len is None:
            raise ValueError("Не объявлена длинна для генерации случайной строки")


        if value == "random" and len <= 0:
            raise ValueError("Ошибка при генерации случайной строки: Длина строки не может быть меньше или равной 0")


        if type(value) == type([]):
            value = list(map(StringDefence.__string, value))

            if False in value:
                raise ValueError("Ошибка при генерации string из списка: Все данные внутри списка должны быть строками\n"
                                 "Только буквы EN, RU в любом регистре")

        return True


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