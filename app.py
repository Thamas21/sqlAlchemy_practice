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
            \r5) Exit''')
        choice = input('What do you want to do? ')
        if choice in ['1', '2', '3', '4', '5']:
           return choice
        else:
            input('''
                \rPlease choose one of the options above.
                \rA number from 1-5.
                \rPress enter to continue. ''')





# main menu, add, search, analysis, exit, view
# add_book function
# edit function
# delete_books function
# search_books
# data_clean
# loop that runs program


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
           pass
        elif choice == '2':
            # view all
            pass
        elif choice == '3':
            # Search for a book
            pass
        elif choice == '4':
            # book analysis
            pass
        else:
            print('Goodbye!')
            app_running = False

    
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app()
