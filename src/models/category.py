from settings import DatabaseConfig
from utils.utils import placeholder_update


class Category(DatabaseConfig):
    """ Category:  """

    def create(self, cat_name):
        """ CREATE category """
        sql = "INSERT INTO category (name) VALUES (?)"
        values = [cat_name, ]

        return self.write(sql, values)

    class read(DatabaseConfig):
        """ 
        read().one(id: int) - read an element by ID

        read().all() - read all elements
        """

        def one(self, id):
            """ SELECT a category by ID """
            sql = "SELECT id, name FROM category WHERE "
            sql += placeholder_update(["id"])
            values = [id, ]

            cur = self.get_cursor()
            row = cur.execute(sql, values).fetchone() or []

            return row

        def all(self):
            """ SELECT all categories """
            sql = "SELECT id, name FROM category"

            cur = self.get_cursor()
            row = cur.execute(sql).fetchall() or []

            return row

    def update(self, id: int, **kwargs) -> bool:
        """ UPDATE category by ID """
        sql = "UPDATE category SET "
        sql += placeholder_update(list(kwargs.keys()))
        sql += " WHERE "
        sql += placeholder_update(["id"])

        values = list(kwargs.values()) + [id]

        return self.write(sql, values)

    def delete(self, id: int) -> bool:
        """ DELETE category by ID """
        sql = "DELETE FROM category WHERE "
        sql += placeholder_update(["id"])
        values = [id, ]

        return self.write(sql, values)
