from generate.defence.integer import IntegerDefence
from generate.defence.string import StringDefence
from generate.defence.float import FloatDefence
from generate.defence.date import DateDefence


classes = {
    "integer": IntegerDefence,
    "string": StringDefence,
    "float": FloatDefence,
    "date": DateDefence
}


class Defence:

    @staticmethod
    def defender(type):
        """Декоратор, который проверяет правильность входящих и исходящих данных"""
        def decorator(func):
            def wrapper(*args, **kwargs):

                Defence.__check_input(type, *args)

                while True:
                    result = func(*args, **kwargs)

                    if Defence.__check_output(type=type, value=result):
                        break

                return result

            return wrapper
        return decorator





    @staticmethod
    def __check_input(type: str, value, len: int = None, number_of_decimal: int = None):
        """ Проверяет входящие данные """

        if type in classes.keys():
            result = classes[type].check_input(value, len, number_of_decimal)
            return result
        else:
            raise ValueError("Неверно указан тип данных для Defence.defender")




    @staticmethod
    def __check_output(type, value):

        if type in classes.keys():
            return classes[type].check_value(value)
        else:
            raise ValueError("Неверно указан тип данных для Defence.defender")

