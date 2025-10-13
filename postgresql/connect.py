import psycopg2

data_type={
    "string":"text",
    "integer":"int",
    "float":"float4",
    "date":"date",
    "time":"time",
    "datetime":"timestamp"
}





def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance



@singleton
class Database:

    # подключение и создание бд ------------------------------------------------------------------------------------------
    def __init__(self, conf: dict):
        self.conn = None
        self.cur = None
        self.conf = conf
        self.connect_to_db(conf)

    def connect_to_db(self, params):
        print('Подключаюсь к PostgreSQL...')

        try:
            self.conn = psycopg2.connect(f"""
                                            host={params["host"]}
                                            port={params["port"]}
                                            {f'sslmode={params["sslmode"]}' if 'sslmode' in params.keys() else ''}
                                            dbname={params["database"]}
                                            user={params["user"]}
                                            password={params["password"]}
                                            target_session_attrs={params["target_session_attrs"]}
                                        """)

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
        except psycopg2.InterfaceError as e:
            print(e)
            print("Не удалось выполнить запрос из-за ошибки подключения. Пытаюсь подключиться к базе заново")
            self.connect_to_db(self.conf)
            self.cur.execute(query, params)






    #-------------------------------------- Работа с БД ------------------------------------------------------------------



    def create_table(self, name: str, data: dict):

        self.execute_query(f"""CREATE TABLE {name} (id serial primary key, {', '.join([i["name"] + ' ' + data_type[i["type"]] for i in data])})""")
