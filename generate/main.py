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
    def integer(values) -> str:
        return Generate.__integer(values)





    @staticmethod
    def __integer(values) -> str:
        if values == "random":
            return str(random.randint(0, 1000000000))


        if type(values) == type([]):
            return str(random.choice(values))


        if "-" in values:
            start, end = list(map(int, values.split("-")))
            return str(random.randint(start, end))

        raise ValueError("Неверное значение для поля values типа данных integer")




    @staticmethod
    @Defence.defender('float')
    def float(values) -> str:
        """Генерирует число с плавающей точкой"""

        if values == "random":
            return str(round(random.uniform(0.0, 10000.0), 4))

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
    def string(values, len = 0) -> str:
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
            start_date, end_date = list(map(lambda x: int(datetime.strptime(x, '%Y-%m-%d').timestamp()), ["1970-01-01", "2025-01-01"]))
            return str(datetime.fromtimestamp(random.randint(start_date, end_date)).date())

        if type(values) == type([]):
            return str(random.choice(values))

        start_date, end_date = list(map(lambda x: int(datetime.strptime(x, '%Y-%m-%d').timestamp()), values.split(split)))

        return str(datetime.fromtimestamp(random.randint(start_date, end_date)).date())





    @staticmethod
    @Defence.defender('datetime')
    def datetime(values):
        """Функция для генерации данных формата дата и время"""

        if values == "random":
            return f"{Generate.__date("random")} {Generate.__time("random")}"

        if type(values) == type([]):
            return str(random.choice(values))

        try:
            start, end = values.split(' ')
            start_date, start_time = start.split('|')
            end_date, end_time = end.split('|')

            return f"{Generate.__date(f"{start_date} {end_date}")} {Generate.__time(f"{start_time} {end_time}")}"
        except:
            raise ValueError("Неверное значение для поля values типа данных datetime")




    @staticmethod
    def __time_to_seconds(time_str) -> int:
        """Конвертирует время из формата hh:mm:ss в секунды"""
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds




    @staticmethod
    def __seconds_to_time(total_seconds) -> str:
        """Конвертирует секунды в формат hh:mm:ss"""
        total_seconds = int(total_seconds)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"





    @staticmethod
    @Defence.defender('time')
    def time(values, split=' ') -> str:
        return Generate.__time(values, split)





    @staticmethod
    def __time(values, split=' '):
        """Функция для генерации данных формата время"""

        if values == "random":
            return Generate.__seconds_to_time(random.randint(0, Generate.__time_to_seconds("23:59:59")))

        if type(values) == type([]):
            return str(random.choice(values))

        try:
            start, end = values.split(split)
            return Generate.__seconds_to_time(random.randint(Generate.__time_to_seconds(start), Generate.__time_to_seconds(end)))

        except:
            raise ValueError("Неверное значение для поля values типа данных time")
