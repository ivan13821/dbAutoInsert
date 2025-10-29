import pandas as pd
from files.csv_file.main import csv_generate



def xlsx(data: dict) -> None:
    """Геенерит xlsxl файл"""

    csv_generate(data)

    df = pd.read_csv('file.csv')
    df.to_excel('file.xlsx', index=False)

