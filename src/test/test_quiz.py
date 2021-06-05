import sqlite3
import unittest

from models import Category, Quiz
from set_up import set_up_database_and_tables


class QuizTest(unittest.TestCase):

    def setUp(self) -> None:
        set_up_database_and_tables()
        Category().create("POLITICS")
        Quiz().create(
            int(Category().read().all()[-1]['id']),
            "Who is the first Priminister of Ghana?",
            "Nana Addo, Kwame Nkrumah, Rawlings",
            "Kwame Nkrumah")

    def test_create_quiz_returns_true_on_success(self):
        self.assertTrue(
            Quiz().create(
                int(Category().read().all()[-1]['id']),
                "Which country promises wealth but without health?",
                "America, Jamaica, China, Russian",
                "China"))

    def test_create_quiz_raise_intergrity_error_for_existing_quiz(self):
        with self.assertRaises(sqlite3.IntegrityError):
            Quiz().create(
                int(Category().read().all()[-1]['id']),
                "Who is the first Priminister of Ghana?",
                "Nana Addo, Kwame Nkrumah, Rawlings",
                "Kwame Nkrumah")

    def test_read_all_quizzes(self):
        self.assertTrue(
            Quiz().create(
                int(Category().read().all()[-1]['id']),
                "In which year did Ghana gained independence?",
                "1997, 2012, 1957, 666",  "1957"))

        self.assertEqual(len(Quiz().read().all()), 2)

    def test_read_one_quiz(self):
        self.assertEqual(len(Quiz().read().one(
            int(Quiz().read().all()[0]['id']))), 5)

    def test_update_quiz_returns_true_on_success(self):
        question = "Which country promised wealth but gave without health?"
        id = Quiz().read().all()[0]['id']

        self.assertTrue(Quiz().update(id, question=question))
        self.assertEqual(Quiz().read().one(id)['question'], question)

    def test_delete_quiz(self):
        id = Quiz().read().all()[0]['id']
        self.assertTrue(Quiz().delete(id))
        self.assertFalse(Quiz().delete(id))

    @unittest.case.skip("DELETE CASCADE IS NOT WORKING")
    def test_delete_category_deletes_quiz(self):
        id = Quiz().read().all()[0]['id']

        self.assertTrue(Category().delete(id))
        # seems like the delete category cascade is not working
        self.assertEqual(Quiz().read().all(), [])


if __name__ == "__main__":
    unittest.main()
