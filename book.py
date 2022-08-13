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
        try:
            if pages > 1:
                self.__pages = pages
            else:
                raise Exception('Page count is NOT valid')
        except Exception as error:
            raise Exception(error)


    def get_pages(self):
        return self.__pages

    def __str__(self):
        return self.get_title() + ' => ' + str(self.get_pages())

    def __eq__(self, other):
        if self.get_title() == other.get_title() and self.get_pages() == other.get_pages():
            return True
        else:
            return False
