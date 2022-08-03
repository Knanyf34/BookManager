class Book:
    def __init__(self, title, pages):
        self.__title = title
        self.__pages = pages

    def set_title(self, title):
        if len(title) > 8:
            self.__title = title
        else:
            print('title most be more than 8 characters')

    def get_title(self):
        return self.__title

    def set_pages(self, pages):
        if pages > 1:
            self.__pages = pages
        else:
            print('pages most be more than 1')

    def get_pages(self):
        return self.__pages
