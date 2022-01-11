from models import (Base, session,
                    Book, engine)
import csv
import datetime
import time

# main menu, analysis 
# edit books
# delete books


def menu():
    while True:
        print('''
            \nPRAGRAMMING BOOKS
            \r1) Add Book
            \r2) View all books
            \r3) Search
            \r4) Analysis
            \r5) Exit

            ''')
        choice = input('What would you like to do?  ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
                    \rPlease choose one of the options above.
                    \rA number from 1-5.
                    \rPress enter to continue...  ''')


def sub_menu():
    while True:
        print('''\nSub Menu
            \n1) Edit
            \r2) Delete
            \r3) Return to main menu''')
        choice = input('What would you like to do?  ')
        if choice in ['1', '2', '3']:
            return choice
        else:
            input('''
                    \rPlease choose one of the options above.
                    \rA number from 1-3.
                    \rPress enter to continue...  ''')


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
            \n***** DATE ERROR *****
            \rInvalid entry please follow (Month Day, Year) format
            \rPress any key to try again...
            \r*******************''')
        return
    else:
        return return_date


def clean_price(price_str):
    try:
        price_float = float(price_str)
    except ValueError:
        input('''
            \n***** Price ERROR *****
            \rInvalid entry price should be a number without a currency symbol
            \rEx: 10.99
            \rPress any key to try again...
            \r*******************''')
        return
    else:
        return int(price_float * 100)


def clean_id(id_str, options):
    try:
        book_id = int(id_str)
    except ValueError:
        input('''
            \n***** ID ERROR *****
            \rInvalid entry please enter an integer (whole number)
            \rPress any key to try again...
            \r*******************''')
        return
    else:
        if book_id in options:
            return book_id
        else:
            input(f'''
                \n***** ID ERROR *****
                \rOptions {options}
                \rPress any key to try again...
                \r*******************''')
            return


def edit_check(column_name, current_value):
    print(f'\n***** EDIT {column_name} *****')
    if column_name == 'Price':
        print(f'\rCurrent Value: {current_value/100}')
    elif column_name == 'Date':
        print(f'\rCurrent Value: {current_value.strftime("%B %d, %Y")}')
    else:
        print(f'\rCurrent Value: {current_value}')

    if column_name == 'Date' or column_name == 'Price':
        while True:
            changes = input('What would you like to change the value to? ')
            if column_name == 'Date':
                changes = clean_date(changes)
                if type(changes) == datetime.date:
                    return changes
            elif column_name == 'Price':
                changes = clean_price(changes)
                if type(changes) == int:
                    return changes
    else:
        return input('What would you like to change the value to? ')


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=date, price=price)
                session.add(new_book)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            title = input('Title: ')
            author = input('Author: ')
            date_error = True
            while date_error:
                date = input('Published Date (Ex: May 1, 2014): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:
                price = input('Price (Ex: 9.99): ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author, published_date=date, price=price)
            session.add(new_book)
            session.commit()
            print('\nBook successfully added!')
            time.sleep(1.5)
        elif choice == '2':
            for book in session.query(Book):
                print(f'''
                    \nBooks in Database
                    \rTitle: {book.title}
                    \rAuthor: {book.author}
                    \rPublished: {book.published_date}
                    \rPrice: ${book.price / 100}''')
        elif choice == '3':
            print('Search Books')
            id_options = []
            for book in session.query(Book):
                id_options.append(book.id)
            id_error = True
            while id_error:
                id_choice = input(f'''
                    \nId Options: {id_options}
                    \rBook id: ''')
                id_choice = clean_id(id_choice, id_options)
                if type(id_choice) == int:
                    id_error = False
            the_book = session.query(Book).filter(Book.id==id_choice).first()
            print(f'''
                    \n{the_book.title} by {the_book.author}
                    \rPublished: {the_book.published_date}
                    \rPrice: ${(the_book.price / 100)}''')
            sub_choice = sub_menu()
            if sub_choice == '1':
                the_book.title = edit_check('Title', the_book.title)
                the_book.author = edit_check('Author', the_book.author)
                the_book.published_date = edit_check('Date', the_book.published_date)
                the_book.price = edit_check('Price', the_book.price)
                session.commit()
                print("Changes successfully made!")
                time.sleep(1.5)
            elif sub_choice == '2':
                session.delete(the_book)
                session.commit()
                print('Book successfull deleted!')
                time.sleep(1.5)
        elif choice == '4':
            print('Analysis')
            oldest_book = session.query(Book).order_by(Book.published_date).first()
            print(f'''
                    \rTitle: {oldest_book.title}
                    \rAuthor: {oldest_book.author}
                    \rPublished: {oldest_book.published_date}
                    \rPrice: ${oldest_book.price / 100}
            ''')
            
            newest_book = session.query(Book).order_by(Book.published_date.desc()).first()
            print(f'''
                    \rTitle: {newest_book.title}
                    \rAuthor: {newest_book.author}
                    \rPublished: {newest_book.published_date}
                    \rPrice: ${newest_book.price / 100}''')
            total_books = session.query(Book).count()
            print(f'Total Books: {total_books}')
            python_books = session.query(Book).filter(Book.title.like('%Python%')).count()
            print(f'Number of books with python in the title: {python_books}')
        else:
            print('Exiting program')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    for row in session.query(Book):
        print(row)
    #app()
    # print(clean_price('28.84'))
