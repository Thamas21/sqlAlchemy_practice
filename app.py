from models import (Base, session,
                    Book, engine)
import datetime



# import models
# main menu add, search, analysis, exit, view
# add books to database
# edit books
# delete books
# search books
# data cleaning
    # price is an integer, date is a datetime object
# loop runs program
if __name__ == '__main__':
    Base.metadata.create_all(engine)