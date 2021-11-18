from models import (Base, session,
                    Book, engine)

# main menu, add, search, analysis, exit, view
# add_book function
# edit function
#  delete_books function
# search_books
# data_clean
# loop that runs program
if __name__ == "__main__":
    Base.metadata.create_all(engine)