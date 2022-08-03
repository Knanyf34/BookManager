# Book Manager

from book import Book

if __name__ == '__main__':
    print('Book Manager App')

    b1 = Book(title='Python Programming', pages=200)
    b2 = Book('Java Spring', 1000)
    b3 = Book('Java Spring', 1000)

    print(b1)
    print(b2)
    print(b3)

    if b2 == b3:
        print('Gholam')
    else:
        print('Ghamar')
