import random




class Generate:


    @staticmethod
    def integer(values, len: int):

        #
        if values == "random":
            return ''.join([str(random.randint(1, 9)) for i in range(int(len))])


        if type(values) == type([]):
            return str(random.choice(values))


        if "-" in values:
            values = list(map(int, values.split("-")))
            start, end = min(values), max(values)
            return str(random.randint(start, end))

        raise ValueError("Неверное для поля values")



    @staticmethod
    def get_string(values, len):
        """Функция генерирует строку данных"""

        if values == "random":
            return ''.join([str(random.choice(list("qwertyuiopasdfghjklzxcvbnm"))) for i in range(int(len))])

        if type(values) == type([]):
            return str(random.choice(values))

        raise ValueError("Неверное для поля values")


    # @staticmethod
    # def gen_data(values):
    #     """"""
