from settings import DatabaseConfig
from utils import placeholder_update


class Quiz(DatabaseConfig):
    """
    >>> quiz = Quiz()
    Quiz Table interface - which inherites the DatabaseConfig class.

    Quiz Table:
        - id: int (PK)
        - cat_id: int (FK)
        - question: str
        - options: str
        - answer: str

    Methods:
        - create
        - update
        - delete

    Class:
        - read

    """

    def create(self, *args) -> bool:
        """
        >>> Quiz().create(*args) -> bool
        >>> Quiz().create(*[cat_id, question, options, answer]) -> bool
        >>> Quiz().create(cat_id, question, options, answer) -> bool
        Create new quiz. Returns False on failure or when there is IntegrityError else True for success.
        """

        sql = "INSERT INTO quiz(cat_id, question, options, answer) VALUES "
        sql += "(?, ?, ?, ?)"

        return self.write(sql, list(args))

    class read(DatabaseConfig):
        """
        >>> row = read().one(id: int) -> sqlite3.Row 
        >>> print(row['id'], row['cat_id'], row['question'], row['options'], row['answer'])
        Returns a sqlite3.Row passing an integer ID

        >>> rows = read().all() -> list
        >>> for row in rows:
        >>>     print(row['id'], row['cat_id'], row['question'], row['options'], row['answer'])
        Returns a list of sqlite3.Rows else and empty list

        Methods:
            - one
            - all
        """

        def one(self, id):
            """
            >>> row = read().one(id: int) -> sqlite3.Row 
            >>> print(row['id'], row['cat_id'], row['question'], row['options'], row['answer'])
            Returns a sqlite3.Row passing an integer ID
            """

            sql = "SELECT id, cat_id, question, options, answer "
            sql += "FROM quiz WHERE "
            sql += placeholder_update(["id"])

            cur = self.get_cursor()
            row = cur.execute(sql, [id]).fetchone() or []

            return row

        def all(self):
            """ 
            >>> rows = read().all() -> list
            >>> for row in rows:
            >>>     print(row['id'], row['cat_id'], row['question'], row['options'], row['answer'])
            Returns a list of sqlite3.Rows else and empty list
            """

            sql = "SELECT id, cat_id, question, options, answer FROM quiz"

            cur = self.get_cursor()
            row = cur.execute(sql).fetchall() or []

            return row

    def update(self, id: int, **kwargs) -> bool:
        """
        >>> Quiz().update(id: int, **kwargs) -> bool
        >>> Quiz().update(id: int, cat_id:int = CAT_ID, question: str = Q_STR, options: str = OP_STR, answer: str = A_STR) -> bool
        Update category, where id is the category's ID. Returns False on failure else True for success.
        """

        sql = "UPDATE quiz SET "
        sql += placeholder_update(list(kwargs.keys()))
        sql += " WHERE "
        sql += placeholder_update(["id"])

        values = list(kwargs.values()) + [id, ]

        return self.write(sql, values)

    def delete(self, id: int) -> bool:
        """
        >>> Quiz().delete(id: int) -> bool
        Delete Quiz by ID. Returns False on failure else True for success.
        """

        sql = "DELETE FROM quiz WHERE "
        sql += placeholder_update(["id"])
        values = [id, ]

        return self.write(sql, values)
