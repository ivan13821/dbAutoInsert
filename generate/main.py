import random
from datetime import datetime
from generate.defence.main import Defence


class Generate:

    @staticmethod
    def __number_for_date(number):
        """Форматирует число: 1 -> 01"""
        if type(number) == type(1):
            number = str(number)

        if len(number) == 1:
            number = '0' + number

        return number


    @staticmethod
    @Defence.defender('integer')
    def integer(values, len=0) -> str:
        return Generate.__integer(values, len)





    @staticmethod
    def __integer(values, len=0) -> str:
        if values == "random" and len > 0:
            return ''.join([str(random.randint(1, 9)) for i in range(int(len))])


        if type(values) == type([]):
            return str(random.choice(values))


        if "-" in values:
            start, end = list(map(int, values.split("-")))
            return str(random.randint(start, end))

        raise ValueError("Неверное значение для поля values типа данных integer")




    @staticmethod
    @Defence.defender('float')
    def float(values, len: int = 0, number_of_decimal: int = 0) -> str:
        """Генерирует число с плавающей точкой"""

        if values == "random" and len > 0:
            return Generate.__integer(values="random", len=len) + "." + Generate.__integer(values="random", len=number_of_decimal)

        if type(values) == type([]):
            return str(random.choice(values))

        if "-" in values:
            start, end = values.split('-')
            start = start.split('.')
            end = end.split('.')
            return Generate.__integer(start[0]+'-'+end[0]) + '.' + Generate.__integer(start[1]+'-'+end[1])

        raise ValueError("Неверное значение для поля values типа данных float")






    @staticmethod
    @Defence.defender('string')
    def string(values, len = 0):
        """Функция генерирует строку данных"""

        if values == "random" and len > 0:
            return ''.join([str(random.choice(list("qwertyuiopasdfghjklzxcvbnm"))) for i in range(int(len))])

        if type(values) == type([]):
            return str(random.choice(values))

        raise ValueError("Неверное значение для поля values типа данных string")





    @staticmethod
    @Defence.defender('date')
    def date(values, split=' ') -> str:
        return Generate.__date(values, split)





    @staticmethod
    def __date(values, split=' ') -> str:
        """Функция для генерации данных формата дата"""

        if values == "random":
            return '-'.join([
                str(random.randint(1970, 2025)),
                Generate.__number_for_date(str(random.randint(1, 12))),
                Generate.__number_for_date(str(random.randint(1, 28)))])

        if type(values) == type([]):
            return str(random.choice(values))

        start_date, end_date = list(map(lambda x: int(datetime.strptime(x, '%Y-%m-%d').timestamp()), values.split(split)))

        return str(datetime.fromtimestamp(random.randint(start_date, end_date)).date())





    @staticmethod
    def datetime(values):
        """Функция для генерации данных формата дата и время"""

        if values == "random":
            return f"{Generate.__date("random")} {Generate.time("random")}"

        if type(values) == type([]):
            return str(random.choice(values))

        try:
            start, end = values.split(' ')
            start_date, start_time = start.split('|')
            end_date, end_time = end.split('|')

            return f"{Generate.__date(f"{start_date} {end_date}")} {Generate.time(f"{start_time} {end_time}")}"
        except:
            raise ValueError("Неверное значение для поля values типа данных datetime")





    @staticmethod
    def time(values, split=' '):
        """Функция для генерации данных формата время"""

        if values == "random":
            return ':'.join([
                Generate.__number_for_date(str(random.randint(0, 23))),
                Generate.__number_for_date(str(random.randint(0, 59))),
                Generate.__number_for_date(str(random.randint(0, 59)))])

        if type(values) == type([]):
            return str(random.choice(values))

        try:
            start_date, end_date = list(map(lambda x: list(map(int, x.split(':'))), values.split(split)))
            return ':'.join([
                Generate.__number_for_date(str(random.randint(start_date[0], end_date[0]))),
                Generate.__number_for_date(str(random.randint(start_date[1], end_date[1]))),
                Generate.__number_for_date(str(random.randint(start_date[2], end_date[2])))])

        except:
            raise ValueError("Неверное значение для поля values типа данных time")
