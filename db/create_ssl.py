import sys
import subprocess
from pathlib import Path

commands = {
    "mysql": {
        "win": "mkdir -p $HOME/.mysql; curl -o $HOME/.mysql/root.crt https://storage.yandexcloud.net/cloud-certs/CA.pem",
        "linux": f"""mkdir -p {Path.home()}/.mysql && wget -q "https://storage.yandexcloud.net/cloud-certs/CA.pem" --output-document {Path.home()}/.mysql/root.crt && chmod 0600 {Path.home()}/.mysql/root.crt"""
    },
    "postgresql": {
        "win": "mkdir $HOME/.postgresql; curl.exe -o $HOME/.postgresql/root.crt https://storage.yandexcloud.net/cloud-certs/CA.pem",
        "linux": f"""mkdir -p {Path.home()}/.postgresql && wget -q "https://storage.yandexcloud.net/cloud-certs/CA.pem" --output-document {Path.home()}/.postgresql/root.crt && chmod 0655 {Path.home()}/.postgresql/root.crt"""
    }
}



class ssl:
    """ Нужен для загрузки SSL сертификата при подключении к БД """

    @staticmethod
    def create_ssl(db) -> None:
        """ Передает команду по пути """

        if sys.platform == "darwin":
            print("Для Mac рекомендуем устанавливать ssl самостоятельно")
            return None

        print("Получение ssl сертификата...")
        try:
            subprocess.run(commands[db][sys.platform], shell=True,)
            print("✅ Сертификат успешно получен!")
        except Exception as e:
            print(f"Произошла ошибка {e}")

