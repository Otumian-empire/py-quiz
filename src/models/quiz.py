from settings import DatabaseConfig
from utils import placeholder_update


class Quiz(DatabaseConfig):
    """ Quiz - id, cat_id, question, options, answer """

    def create(self, *args):
        """ CREATE quiz
        cat_id: int
        question: str
        options: str,
        answer: str """

        sql = "INSERT INTO quiz(cat_id, question, options, answer) VALUES "
        sql += "(?, ?, ?, ?)"

        return self.write(sql, list(args))

    class read(DatabaseConfig):
        """ 
        read().one(id:int) - read an element by ID

        read().all() - read all elements
        """

        def one(self, id):
            """ SELECT a quiz by ID """
            sql = "SELECT id, cat_id, question, options, answer "
            sql += "FROM quiz WHERE "
            sql += placeholder_update(["id"])

            cur = self.get_cursor()
            row = cur.execute(sql, [id]).fetchone() or []

            return row

        def all(self):
            """ SELECT all quizzes """
            sql = "SELECT id, cat_id, question, options, answer FROM quiz"

            cur = self.get_cursor()
            row = cur.execute(sql).fetchall() or []

            return row

    def update(self, id: int, **kwargs) -> bool:
        """ UPDATE quiz  """
        sql = "UPDATE quiz SET "
        sql += placeholder_update(list(kwargs.keys()))
        sql += " WHERE "
        sql += placeholder_update(["id"])

        values = list(kwargs.values()) + [id, ]

        return self.write(sql, values)

    def delete(self, id: int) -> bool:
        sql = "DELETE FROM quiz WHERE "
        sql += placeholder_update(["id"])
        values = [id, ]

        return self.write(sql, values)
