""" Файл запуска парсера """

class Callback:
    """ Класс, содержащий списки возвращаемых значений
    и callback функции """

    def __init__(self):
        self.open_tag_list = []
        self.attrs_list = []
        self.data_list = []
        self.close_tag_list = []

    def find_open_tag(self, tag, attrs):
        """ Callback open tag """
        self.open_tag_list += [tag]
        self.attrs_list += [attrs]
        #print("I find open tag: ", tag, " and attributes: ", attrs)

    def find_data(self, data):
        """ Callback data """
        self.data_list += [data]
        #print("I find data: ", data)

    def find_close_tag(self, tag):
        """ Callback close tag """
        self.close_tag_list += [tag]
        #print("I find close tag: ", tag)

def parse_html(html_str: str, open_tag_callback,
               data_callback, close_tag_callback):
    """ Главная функция, решающая задачу парсинга """
    open_tag = False
    attrs = False
    close_tag = False
    data = False
    open_tag_str = ""
    attrs_str = ""
    close_tag_str = ""
    data_str = ""
    for i, symbol in enumerate(html_str):
        if symbol == '>':
            if open_tag or attrs:
                open_tag_callback(open_tag_str, attrs_str)
            if close_tag:
                close_tag_callback(close_tag_str)
            open_tag = False
            attrs = False
            close_tag = False
            data = True
            data_str = ""
            continue

        if symbol == '<':
            if data and not data_str == "":
                data_callback(data_str)
            data = False
            if html_str[i:i+2] == "</":
                close_tag = True
                open_tag = False
                close_tag_str = ""
                continue
            open_tag = True
            attrs = False
            close_tag = False
            open_tag_str = ""
            continue

        if html_str[i-1:i+1] == "</":
            continue

        if open_tag and symbol == ' ' and not attrs:
            attrs = True
            open_tag = False
            attrs_str = ""
            continue

        data_str = data_str + symbol if data else data_str
        open_tag_str = open_tag_str + symbol if open_tag else open_tag_str
        close_tag_str = close_tag_str + symbol if close_tag else close_tag_str
        attrs_str = attrs_str + symbol if attrs else attrs_str

if __name__ == "__main__":
    cb = Callback()
    html_string = input()
    parse_html(html_string, cb.find_open_tag, cb.find_data, cb.find_close_tag)
    print(cb.open_tag_list)
    print(cb.attrs_list)
    print(cb.data_list)
    print(cb.close_tag_list)
