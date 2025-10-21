import pymysql
from pathlib import Path
from create_ssl import ssl

data_type={
    "string":"TEXT",
    "integer":"INT",
    "float":"DOUBLE",
    "date":"DATE",
    "time":"TIME",
    "datetime":"DATETIME"
}





def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance



@singleton
class Mysql:

    # подключение и создание бд ------------------------------------------------------------------------------------------
    def __init__(self, conf: dict):
        self.conn = None
        self.cur = None
        self.conf = conf
        self.connect_to_db(conf)




    def connect_to_db(self, params):
        print('Подключаюсь к MySQL...')

        try:
            if params["host"] == 'localhost':
                self.conn = pymysql.connect(
                    host=params["host"],
                    port=int(params["port"]),
                    user=params['user'],
                    password=params['password'],
                    database=params['database'],
                    charset='utf8mb4',
                    autocommit=True
                )
            else:
                ssl.create_ssl("mysql")
                ssl_ca_path = Path('~/.mysql/root.crt').expanduser()
                self.conn = pymysql.connect(
                                        host=params["host"],
                                        port=int(params["port"]),
                                        user=params['user'],
                                        password=params['password'],
                                        database=params['database'],
                                        charset='utf8mb4',
                                        ssl={'ca': ssl_ca_path},
                                        autocommit=True
                                    )

            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            print(f'Успешно подключен!')

        except Exception as error:
            print(error)




    def execute_query(self, query, params=None):
        try:
            if params is not None:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
        except:
            print("Не удалось выполнить запрос из-за ошибки подключения. Пытаюсь подключиться к базе заново")
            self.connect_to_db(self.conf)
            self.cur.execute(query, params)






    #-------------------------------------- Работа с БД ------------------------------------------------------------------



    def create_table(self, name: str, data: dict):

        self.execute_query(f"""CREATE TABLE {name} (id serial primary key, {', '.join([i["name"] + ' ' + data_type[i["type"]] for i in data])});""")