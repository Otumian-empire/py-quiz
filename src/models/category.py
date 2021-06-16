from settings import DatabaseConfig
from utils import placeholder_update


class Category(DatabaseConfig):
    """
    >>> cat = Category()
    Category Module interface - which inherites the DatabaseConfig class.

    Category Table:
        - id: int (PK)
        - name: str

    Methods:
        - create
        - update
        - delete

    Class:
        - read

    """

    def create(self, cat_name: str) -> bool:
        """
        >>> Category().create(cat_name:str) -> bool
        Create new category. Returns False on failure or when there is IntegrityError else True for success.
        """

        sql = "INSERT INTO category (name) VALUES (?)"
        values = [cat_name, ]

        return self.write(sql, values)

    class read(DatabaseConfig):
        """
        >>> row = read().one(id: int) -> sqlite3.Row 
        >>> print(row['id'], row['name'])
        Returns a sqlite3.Row passing an integer ID

        >>> rows = read().all() -> list
        >>> for row in rows:
        >>>     print(row['id'], row['name'])
        Returns a list of sqlite3.Rows else and empty list

        Methods:
            - one
            - all
        """

        def one(self, id: int):
            """
            >>> row = read().one(id: int) -> sqlite3.Row 
            >>> print(row['id'], row['name'])
            Returns a sqlite3.Row passing an integer ID
            """

            sql = " ".join(["SELECT id, name FROM category WHERE",
                            placeholder_update(["id"])])

            values = [id, ]

            cur = self.get_cursor()
            row = cur.execute(sql, values).fetchone() or []

            return row

        def all(self):
            """ 
            >>> rows = read().all() -> list
            >>> for row in rows:
            >>>     print(row['id'], row['name'])
            Returns a list of sqlite3.Rows else and empty list
            """

            sql = "SELECT id, name FROM category"

            cur = self.get_cursor()
            row = cur.execute(sql).fetchall() or []

            return row

    def update(self, id: int, **kwargs) -> bool:
        """
        >>> Category().update(id: int, **kwargs) -> bool
        >>> Category().update(id: int, name: str = "some str") -> bool
        Update category, where id is the category's ID. Returns False on failure else True for success.
        """

        sql = " ".join(["UPDATE category SET",
                        placeholder_update(list(kwargs.keys())),
                        "WHERE",
                        placeholder_update(["id"])])

        values = list(kwargs.values()) + [id]

        return self.write(sql, values)

    def delete(self, id: int) -> bool:
        """
        >>> Category().delete(id: int) -> bool
        Delete category by ID. Returns False on failure else True for success.
        """

        sql = " ".join(["DELETE FROM category WHERE",
                       placeholder_update(["id"])])
                       
        values = [id, ]

        return self.write(sql, values)
