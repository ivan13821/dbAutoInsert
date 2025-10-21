import json






class JSONTemplates:
    """Позволяет создавать и повторно использовать шаблоны для заполнения json """

    @staticmethod
    def replace_templates(data):
        """ Осуществляет поиск шаблонов внутри json """

        pass







    @staticmethod
    def __get_templates():
        """ Передает шаблоны в другие функции """
        with open('templates/templates.json', 'r', encoding='utf-8') as file:
            return json.load(file)