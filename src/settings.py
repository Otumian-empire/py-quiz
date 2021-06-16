import sqlite3


DATABASE = "quiz_db"


class DatabaseConfig:
    """ DatabaseConfig sets the connection, and cursor """

    def __init__(self):
        """
        >>> DatabaseConfig()
        Takes no argument and Initializes the database connection and sets the row_factory to sqlite3.Row
        """
        try:
            self.conn = sqlite3.connect(DATABASE)
            self.conn.row_factory = sqlite3.Row

        except sqlite3.Error as e:
            print(e)

    def get_conn(self):
        """
        >>> DatabaseConfig().get_conn()
        returns the database connection, sqlite3.connect(db) else False when there is an exception
        """
        try:
            return self.conn
        except (Exception, sqlite3.Error) as e:
            print(str(e))
            return False

    def get_cursor(self):
        """
        >>> DatabaseConfig().get_cursor()
        returns the database cursor, sqlite3.connect(db).cursor() else False when there is an exception
        """
        try:
            self.cur = self.conn.cursor()
            return self.cur
        except (Exception, sqlite3.Error) as e:
            print(str(e))
            return False

    def write(self, sql: str, vals: list) -> bool:
        """ 
        >>> DatabaseConfig().write(sql_query: str, vals: list) -> bool
        Takes sql query with it's in-place values in a list. This is similar to 
        >>> sql = "INSERT INTO tb_name (field1, fields2, ..., fieldN) VALUES (?, ?, ..., ?N)"
        >>> vals = [val1, val2, ..., valN]
        >>> DatabaseConfig().write(sql, vals)
        This works for Writing to the database (CREATE, UPDATE and DELETE). The boolean is a result of
        >>> cur.rowcount > 0
        """

        cur = self.get_cursor()
        cur.execute(sql, vals)

        res = cur.rowcount > 0
        self.get_conn().commit()
        self.get_conn().close()

        return res
