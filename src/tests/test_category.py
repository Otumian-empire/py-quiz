import unittest
import sqlite3

from models import Category
from set_up import set_up_database_and_tables


class CategoryTest(unittest.TestCase):

    def setUp(self) -> None:
        set_up_database_and_tables()
        Category().create("POLITICS")
        Category().create("BUSINESS")

    def test_create_category_returns_true_on_success(self):
        self.assertTrue(Category().create("SCIENCE"))

    def test_create_category_raises_intergrity_error_for_existing_category(self):
        with self.assertRaises(sqlite3.IntegrityError):
            Category().create("POLITICS")

    def test_read_all_categories(self):
        self.assertEqual(len(Category().read().all()), 2)

    def test_read_one_category_returns_only_one_category(self):
        ID = 1
        NAME = "POLITICS"

        self.assertEqual(Category().read().one(ID)['name'], NAME)

    def test_update_category_returns_true_on_success_and_changes_required_fields(self):
        ID = 1
        NAME = "GOVERNMENTS"

        self.assertTrue(Category().update(ID, name=NAME))
        self.assertEqual(Category().read().one(ID)['name'], NAME)

    def test_delete_category_returns_true_on_success(self):
        ID = 1

        self.assertTrue(Category().delete(ID))
        self.assertFalse(Category().delete(ID))


if __name__ == "__main__":
    unittest.main()
