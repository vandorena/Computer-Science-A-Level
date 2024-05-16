import os

def delete_database(db_name):
    if os.path.exists(db_name):
        os.remove(db_name)
    else:
        print("The database does not exist")

delete_database("this.db")