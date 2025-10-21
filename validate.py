from pydantic import BaseModel, ValidationError, validator
from typing import List, Literal, Union, Optional




class Conf(BaseModel):
    host: str
    port: str
    user: str
    database: str
    password: str


class DataItem(BaseModel):
    name: str
    type: Literal["string", "date", "integer", "float", "time", "datetime"]
    len: Optional[int] = None
    values: Union[str, List[str]]

class Tables(BaseModel):
    name: str
    rows_count: int
    columns: List[DataItem]


class Template(BaseModel):
    database: Literal["postgresql", "mysql"]
    conf: Conf
    tables: List[Tables]


class Template_csv(BaseModel):
    database: Literal["csv"]
    columns: List[DataItem]



def validate_json(input_json, type='database'):
    if type == "csv":
        try:
            Template_csv(**input_json)
            return True, "JSON соответствует шаблону"
        except ValidationError as e:
            return False, f"Ошибка валидации: {e}"
    else:
        try:
            Template(**input_json)
            return True, "JSON соответствует шаблону"
        except ValidationError as e:
            return False, f"Ошибка валидации: {e}"


