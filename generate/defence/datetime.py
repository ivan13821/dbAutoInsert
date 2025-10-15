from generate.defence.date import DateDefence
from generate.defence.time import TimeDefence




class DateTimeDefence(DateDefence, TimeDefence):

    @staticmethod
    def check_input(value, len: int = 0, number_of_decimal: int = None) -> bool:
        """ Проверяет все возможные значения value для datetime типа данных """

        if value == "random":
            return True


        if type(value) == type([]):
            result = list(map(DateTimeDefence.__datetime, value))

            if False in result:
                raise ValueError(f"Ошибка при генерации datetime из списка: Некорректное время или дата в списке:{value}")
            else:
                return True


        if " " in value:
            start, end = value.split(" ")

            if DateTimeDefence.__datetime(start, "|") == False or DateTimeDefence.__datetime(end, "|") == False:
                raise ValueError(f"Ошибка при генерации datetime из диапазона: Некорректное время или дата внутри диапазона: {value}")
            else:
                return True

        raise ValueError(f"Ошибка при генерации datetime: Unknow error. value={value}")





    @staticmethod
    def check_value(datetime):
        return DateTimeDefence.__datetime(datetime)





    @staticmethod
    def __datetime(datetime, split=" ") -> bool:
        """Проверяет корректность даты и времени"""

        datetime = datetime.split(split)

        if len(datetime) != 2:
            return False

        date, time = datetime


        return DateDefence.check_value(date) and TimeDefence.check_value(time)
