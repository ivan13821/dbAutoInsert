from generate.defence.integer import IntegerDefence
from generate.defence.string import StringDefence
from generate.defence.float import FloatDefence
from generate.defence.date import DateDefence
from generate.defence.time import TimeDefence
from generate.defence.datetime import DateTimeDefence

classes = {
    "integer": IntegerDefence,
    "string": StringDefence,
    "float": FloatDefence,
    "date": DateDefence,
    "time": TimeDefence,
    "datetime": DateTimeDefence
}


class Defence:

    @staticmethod
    def defender(type):
        """Декоратор, который проверяет правильность входящих и исходящих данных"""
        def decorator(func):
            def wrapper(*args, **kwargs):

                Defence.__check_input(type, *args)

                result = func(*args, **kwargs)

                return result

            return wrapper
        return decorator





    @staticmethod
    def __check_input(type: str, value, len: int = None):
        """ Проверяет входящие данные """

        if type in classes.keys():
            result = classes[type].check_input(value, len)
            return result
        else:
            raise ValueError("Неверно указан тип данных для Defence.defender")



