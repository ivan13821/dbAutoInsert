import random



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
    def integer(values, len=0) -> str:
        if values == "random":
            return ''.join([str(random.randint(1, 9)) for i in range(int(len))])


        if type(values) == type([]):
            return str(random.choice(values))


        if "-" in values:
            values = list(map(int, values.split("-")))
            start, end = min(values), max(values)
            return str(random.randint(start, end))

        raise ValueError("Неверное значение для поля values типа данных integer")




    @staticmethod
    def float(values, len: int = 0, number_of_decimal: int = 0) -> str:
        """Генерирует число с плавающей точкой"""

        if values == "random":
            return Generate.integer(values="random", len=len) + "." + Generate.integer(values="random", len=number_of_decimal)

        if type(values) == type([]):
            return str(random.choice(values))

        if "-" in values:
            start, end = values.split('-')
            start = start.split('.')
            end = end.split('.')
            return Generate.integer(start[0]+'-'+end[0]) + '.' + Generate.integer(start[1]+'-'+end[1])

        raise ValueError("Неверное значение для поля values типа данных float")






    @staticmethod
    def string(values, len = 0):
        """Функция генерирует строку данных"""

        if values == "random":
            return ''.join([str(random.choice(list("qwertyuiopasdfghjklzxcvbnm"))) for i in range(int(len))])

        if type(values) == type([]):
            return str(random.choice(values))

        raise ValueError("Неверное значение для поля values типа данных string")





    @staticmethod
    def date(values, split=' ') -> str:
        """Функция для генерации данных формата дата"""

        if values == "random":
            return '-'.join([
                str(random.randint(1970, 2025)),
                Generate.__number_for_date(str(random.randint(1, 12))),
                Generate.__number_for_date(str(random.randint(1, 28)))])

        if type(values) == type([]):
            return str(random.choice(values))

        try:
            start_date, end_date = list(map(lambda x: list(map(int, x.split('-'))), values.split(split)))
            return '-'.join([
                str(random.randint(start_date[0], end_date[0])),
                Generate.__number_for_date(str(random.randint(start_date[1], end_date[1]))),
                Generate.__number_for_date(str(random.randint(start_date[2], end_date[2])))])

        except:
            raise ValueError("Неверное значение для поля values типа данных date")





    @staticmethod
    def datetime(values):
        """Функция для генерации данных формата дата и время"""

        if values == "random":
            return f"{Generate.date("random")} {Generate.time("random")}"

        if type(values) == type([]):
            return str(random.choice(values))

        try:
            start, end = values.split(' ')
            start_date, start_time = start.split('|')
            end_date, end_time = end.split('|')

            return f"{Generate.date(f"{start_date} {end_date}")} {Generate.time(f"{start_time} {end_time}")}"
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
