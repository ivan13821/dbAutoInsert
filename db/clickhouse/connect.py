from clickhouse_driver import Client

data_type={
    "string":"String",
    "integer":"Int32",
    "float":"Float64",
    "date":"Date",
    "time":None,
    "datetime":"DateTime"
}





def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance



@singleton
class ClickHouse:

    # подключение и создание бд ------------------------------------------------------------------------------------------
    def __init__(self, conf: dict):
        self.conn = None
        self.cur = None
        self.conf = conf
        self.connect_to_db(conf)




    def connect_to_db(self, params):
        print('Подключаюсь к ClickHouse...')

        try:
            if params["host"] == 'localhost':
                self.conn = Client(
                    host=params["host"],
                    port=int(params["port"]),
                    user=params['user'],
                    password=params['password'],
                    database=params['database']
                )
            else:
                self.conn = Client(
                                        host=params["host"],
                                        port=int(params["port"]),
                                        user=params['user'],
                                        password=params['password'],
                                        database=params['database'],
                                        secure=True,
                                        verify=True,
                                        ca_certs="/usr/local/share/ca-certificates/Yandex/RootCA.crt"
                                    )

            self.conn.autocommit = True
            self.cur = self.conn.execute
            print(f'Успешно подключен!')

        except Exception as error:
            print(error)




    def execute_query(self, query, params=None):
        try:
            if params is not None:
                self.cur(query, params)
            else:
                self.cur(query)
        except:
            print("Не удалось выполнить запрос из-за ошибки подключения. Пытаюсь подключиться к базе заново")
            self.connect_to_db(self.conf)
            self.cur(query, params)






    #-------------------------------------- Работа с БД ------------------------------------------------------------------



    def create_table(self, name: str, data: dict):
        query = []
        for i in data:
            if data_type[i["type"]] is None:
                continue
            query.append(f"`{i["name"]}` {data_type[i["type"]]}")

        query = f"""CREATE TABLE `{name}` ({', '.join(query)}) ENGINE = MergeTree() ORDER BY `Имя`;"""

        self.execute_query(query)