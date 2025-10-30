from db.postgresql.connect import Postgresql
from generate.main import Generate
from tqdm import tqdm


data_type={
    "string":"text",
    "integer":"int",
    "float":"DOUBLE PRECISION",
    "date":"date",
    "time":"time",
    "datetime":"timestamp"
}




def postgresql(conf: dict, data: dict) -> None:
    """Функция подключается к БД, создает таблицу, и наливает в нее данные"""

    global db

    db = Postgresql(conf=conf)


    for i in data:
        name, data, rows_count = i["name"], i["columns"], i["rows_count"]
        db.execute_query(f"DROP TABLE IF EXISTS {name};")
        db.create_table(name=name, data=data)
        insert_data(name=name, data=data, rows_count=rows_count)





def insert_data(name: str, data: dict, rows_count: int) -> None:
    """Функция для заполнения таблиц данными"""
    global db

    big_mass = []
    query = f"""INSERT INTO {name} ({', '.join(['"'+i["name"]+'"' for i in data])}) values """

    pbar = tqdm(total=rows_count)
    for i in range(rows_count):

        #Если данных слишком много, отправляем запрос, чтобы прога по оперативке не упала
        if len(big_mass) > 10000:
            query += ', '.join(big_mass) + ';'
            db.execute_query(query)
            big_mass = []
            query = f"""INSERT INTO {name} ({', '.join(['"'+i["name"]+'"' for i in data])}) values """


        big_mass.append(generate_values(data))
        pbar.update(1)

    query += ', '.join(big_mass) + ';'

    db.execute_query(query)




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

    return f"('{"', '".join(mass)}')"










