import json
from validate import validate_json
from db.postgresql.main import postgresql
from db.clickhouse.main import clickhouse
from csv_file.main import csv_generate
from db.my_sql.main import mysql
from time import time
from templates.main import JSONTemplates
from xlsx.main import xlsx

databases = {
    "postgresql": postgresql,
    "mysql":mysql,
    "clickhouse": clickhouse
}



def main():
    with open('conf.json', 'r', encoding='utf-8') as file:
        print("Генерация данных началась...")
        work_time = time()
        data = json.load(file)

        #Заменяет шаблоны на корректные данные
        JSONTemplates.replace_templates(data)

        # Если это csv то он генерится иначе
        if data["database"] in ["csv", "xlsx"]:

            # проверяем правильность входных данных
            if not (answer := validate_json(data, type='csv'))[0]:
                print(answer[1])
                return 0
            if data["database"] == "xlsx":
                xlsx(data)
            else:
                csv_generate(data)


        else:

            # проверяем правильность входных данных
            if not (answer := validate_json(data))[0]:
                print(answer[1])
                return 0

            #вызываем БД в зависимости от json
            databases[data["database"]](conf=data["conf"], data=data["tables"])

        print(f"Генерация данных завершена за {round(time() - work_time, 3)} сек.")












if __name__ == "__main__":
    main()