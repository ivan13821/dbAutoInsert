from postgresql.connect import Database
from postgresql.generate import Generate



data_type={
    "string":"text",
    "integer":"int",
    "float":"float4",
    "date":"date",
    "time":"time",
    "datetime":"timestamp"
}




def postgresql(conf: dict, data: dict) -> None:
    """Функция подключается к БД, создает таблицу, и наливает в нее данные"""

    global db

    db = Database(conf=conf)


    for i in data:
        name, data = i["name"], i["data"]
        #db.create_table(name=name, data=data)
        insert_data(name=name, data=data)





def insert_data(name: str, data: dict) -> None:
    """Функция для заполнения таблиц данными"""

    big_mass = []
    query = f"""INSERT INTO {name} ({', '.join([i["name"] for i in data])}) values """

    for i in range(100):

        big_mass.append(generate_values(data))

    query += ', '.join(big_mass) + ';'
    print(query)

    global db

    db.insert(query)




def generate_values(data):
    """Генерирует одну строку данных"""


    mass = []
    for pole in data:

        if pole["type"] == "integer":
            mass.append(Generate.integer(pole["values"], pole["len"]))

        elif pole["type"] == "string":
            mass.append(Generate.get_string(pole["values"], pole["len"]))

        elif pole["type"] == "date":
            mass.append('2019-01-01')

    return f"('{"', '".join(mass)}')"








