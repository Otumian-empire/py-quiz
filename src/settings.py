import sqlite3


DATABASE = "quiz_db"


class DatabaseConfig:
    """ DatabaseConfig sets the connection, and cursor """

    def __init__(self):
        try:
            self.conn = sqlite3.connect(DATABASE)
            self.conn.row_factory = sqlite3.Row

        except sqlite3.Error as e:
            print(e)

    def get_conn(self):
        """ return connection """
        try:
            return self.conn
        except (Exception, sqlite3.Error) as e:
            print(str(e))
            return False

    def get_cursor(self):
        """ return cursor """
        try:
            self.cur = self.conn.cursor()
            return self.cur
        except (Exception, sqlite3.Error) as e:
            print(str(e))
            return False

    def write(self, sql: str, vals: list) -> bool:
        """ Write (CREATE, UPDATE and DELETE) - bool (rows affected > 0) """

        cur = self.get_cursor()
        cur.execute(sql, vals)

        res = cur.rowcount > 0
        self.get_conn().commit()
        self.get_conn().close()

        return res
