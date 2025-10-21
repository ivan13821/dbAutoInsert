import json
from validate import validate_json
from postgresql.main import postgresql
from csv_file.main import csv_generate
from my_sql.main import mysql
from time import time


databases = {
    "postgresql": postgresql,
    "mysql":mysql
}



def main():
    with open('conf.json', 'r', encoding='utf-8') as file:
        print("Генерация данных началась...")
        work_time = time()
        data = json.load(file)


        # Если это csv то он генерится иначе
        if data["database"] == "csv":

            # проверяем правильность входных данных
            if not (answer := validate_json(data, type='csv'))[0]:
                print(answer[1])
                return 0
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