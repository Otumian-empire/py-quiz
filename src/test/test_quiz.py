import unittest
import sqlite3

from models.quiz import Quiz
from models.category import Category
from set_up import set_up_database_and_tables


class QuizTest(unittest.TestCase):
    set_up_database_and_tables()

    Category().create("POLITICS")

    def test_0_create_quiz(self):
        cat_id = 1
        question = "Which country promises wealth but without health?"
        options = ", ".join(["America", "Jamaica", "China", "Russian"])
        answer = "China"

        self.assertTrue(Quiz().create(cat_id, question, options, answer))

    def test_1_create_quiz(self):
        with self.assertRaises(sqlite3.IntegrityError):
            cat_id = 1
            question = "Which country promises wealth but without health?"
            options = ", ".join(["America", "Jamaica", "China", "Russian"])
            answer = "China"
            Quiz().create(cat_id, question, options, answer)

    def test_2_read_all_quizzes(self):
        rows = Quiz().read().all()

        self.assertEqual(len(rows), 1)

    def test_3_read_one_quiz(self):
        ID = 1
        QUESTION = "Which country promises wealth but without health?"

        row = Quiz().read().one(ID)

        self.assertEqual(row['question'], QUESTION)

    def test_4_update_quiz(self):
        ID = 1
        QUESTION = "Which country promised wealth but gave without health?"

        self.assertTrue(Quiz().update(ID, question=QUESTION))
        self.assertEqual(Quiz().read().one(ID)['question'], QUESTION)

    def test_5_delete_quiz(self):
        ID = 1

        self.assertTrue(Quiz().delete(ID))
        self.assertFalse(Quiz().delete(ID))


if __name__ == "__main__":
    unittest.main()
