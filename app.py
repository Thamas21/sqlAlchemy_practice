from models import (Base, session,
                    Book, engine)
import datetime
import csv
import time
# search, analysis,
# edit function
# delete_books function
# search_books


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


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input('''
            \n***  DATE ERROR *** 
            \rThe date format should include a valid Month, Date, Year from the past
            \r Ex: Januarly 13, 2003
            \r Press enter to try again
            \r *****************''')
        return
    else:
        return return_date


def clean_price(price_str):
    try:
        price_float = float(price_str)

    except ValueError:
        input('''
            \n***  Price Error *** 
            \rThe price format should include a number without a currency symbol
            \r Ex: 10.99
            \r Press enter to try again
            \r *****************''')
    else:
        return int(price_float * 100)


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title == row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, date_published=date, price=price)
                session.add(new_book)
    session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            title = input('Title: ')
            authtor = input('Author: ')
            date_error = True
            while date_error:
                date = input('Published Date (Ex: October 25, 2017): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:
                price = input('Price: (Ex: 25.28): ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=authtor, date_published=date, price=price)
            session.add(new_book)
            session.commit()
            print("The book was added!")
            time.sleep(2)

        elif choice == '2':
            # view all
            for book in session.query(Book):
                print(f'''\n{book.id}:
                        \rTitle: {book.title}
                        \rAuthor: {book.author}
                        ''')
            input('Press enter to return to the main menu')
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

    add_csv()
    app()
    for book in session.query(Book):
        print(book)
