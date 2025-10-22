import json






class JSONTemplates:
    """Позволяет создавать и повторно использовать шаблоны для заполнения json """




    @staticmethod
    def __get_template_on_string(string: str, templates: dict) -> str:
        """Проверяет является ли строка шаблоном и отправляет шаблон если да"""

        if string[0:3] == "{{ " and string[-3:] == " }}":
            key = string[3:-3]
            if key in templates.keys():
                return templates[key]
            else:
                raise ValueError(f"Нет шаблона по ключу: {key}")
        return ''




    @staticmethod
    def __replace_templates(mass: dict, templates: dict) -> dict:
        """Находит шаблоны в словаре и заменяет их на нужное значение"""

        range_mass = mass.keys() if type(mass) == type({}) else range(len(mass))

        for i in range_mass:

            if type(mass[i]) == type({}) or type(mass[i]) == type([]):
                JSONTemplates.__replace_templates(mass[i], templates)

            elif type(mass[i]) == type(''):
                if answer := JSONTemplates.__get_template_on_string(mass[i], templates=templates):
                    mass[i] = answer

        return mass





    @staticmethod
    def replace_templates(mass: dict) -> dict:
        """ Создана, чтобы не вызывать парсинг json шаблонов при каждом запуске __replace_templates"""

        return JSONTemplates.__replace_templates(mass=mass, templates=JSONTemplates.__get_templates())







    @staticmethod
    def __get_templates():
        """ Передает шаблоны в другие функции """
        with open('templates/templates.json', 'r', encoding='utf-8') as file:
            return json.load(file)