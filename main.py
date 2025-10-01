import json
from validate import validate_json
from postgresql.main import postgresql


databases = {
    "postgresql": postgresql
}



def main():
    with open('conf.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        #проверяем правильность входных данных
        if not (answer := validate_json(data))[0]:
            print(answer[1])
            return 0

        #вызываем БД в зависимости от json
        databases[data["database"]](conf=data["conf"], data=data["data"])












if __name__ == "__main__":
    main()