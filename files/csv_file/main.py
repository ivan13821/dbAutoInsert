from generate.main import Generate
from tqdm import tqdm
import csv




def csv_generate(data: dict) -> None:
    """Функция подключается к БД, создает таблицу, и наливает в нее данные"""


    with open("file.csv", "w", encoding='utf-8') as file:
        try:
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")

            pbar = tqdm(total=data["rows_count"])

            names = {}

            # генерим заголовки
            row = []
            for i in data["columns"]:
                if i["name"] in names.keys():
                    row.append(i["name"]+str(names[i["name"]]))
                    names[i["name"]] += 1
                else:
                    row.append(i["name"])
                    names[i["name"]] = 1

            file_writer.writerow(row)
            pbar.update(1)

            # Генерим содержимое файла
            for j in range(data["rows_count"]):
                file_writer.writerow(generate_values(data["columns"]))
                pbar.update(1)
        except:
            raise "unknow error"







def insert_data(name: str, data: dict, rows_count: int) -> None:
    """Функция для заполнения таблиц данными"""

    big_mass = []

    for i in range(rows_count):

        big_mass.append(generate_values(data))




def generate_values(data):
    """Генерирует одну строку данных"""


    mass = []
    for pole in data:

        if pole["type"] == "integer":
            if "len" in pole.keys():
                mass.append(Generate.integer(pole["values"], pole["len"]))
            else:
                mass.append(Generate.integer(pole["values"]))


        elif pole["type"] == "float":
            if "len" in pole.keys() and "number_of_decimal" in pole.keys():
                mass.append(Generate.float(pole['values'], pole["len"], pole["number_of_decimal"]))
            else:
                mass.append(Generate.float(pole['values']))


        elif pole["type"] == "string":
            if "len" in pole.keys():
                mass.append(Generate.string(pole["values"], pole["len"]))
            else:
                mass.append(Generate.string(pole["values"]))


        elif pole["type"] == "date":
            mass.append(Generate.date(pole["values"]))


        elif pole["type"] == "time":
            mass.append(Generate.time(pole['values']))


        elif pole["type"] == "datetime":
            mass.append(Generate.datetime(pole['values']))

    return mass