import sys
from models import (Base, session,
                    Book, engine)


def menu():
    while True:
        print('''
            \nPROMANNING BOOK
            \r1) Add a book
            \r2) View all books
            \r3) Search for a book
            \r4) Book Analysis
            \r5) Exit
            ''')
        input('What do you want to do? ')

def add():
    pass

def view_all():
    pass

def search():
    pass

def analysis():
    pass


def exit(input):
    if input == 5:
        sys.exit()





# main menu, add, search, analysis, exit, view
# add_book function
# edit function
# delete_books function
# search_books
# data_clean
# loop that runs program


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu()
