import sqlite3
from settings import DATABASE

def set_up_database_and_tables() -> None:
    """ Create database and tables """
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        with open("quiz_db.sql") as sqlfp:
            cur.executescript(sqlfp.read())
            con.commit()

        print("DATABASE OK")
    except (sqlite3.Error, Exception,) as e:
        print(e)
    finally:
        con.close()


if __name__ == "__main__":
    set_up_database_and_tables()
