import unittest
import sqlite3

from models.category import Category
from set_up import set_up_database_and_tables


class CategoryTest(unittest.TestCase):
    set_up_database_and_tables()

    def test_0_create_category(self):
        self.assertTrue(Category().create("POLITICS"))
        self.assertTrue(Category().create("BUSINESS"))
        self.assertTrue(Category().create("COMPUTER SCIENCE"))

    def test_1_create_category(self):
        with self.assertRaises(sqlite3.IntegrityError):
            Category().create("POLITICS")

        with self.assertRaises(sqlite3.IntegrityError):
            Category().create("BUSINESS")

        with self.assertRaises(sqlite3.IntegrityError):
            Category().create("COMPUTER SCIENCE")

    def test_2_read_all_categories(self):
        rows = Category().read().all()

        self.assertEqual(len(rows), 3)

    def test_3_read_one_category(self):
        ID = 1
        NAME = "POLITICS"
        row = Category().read().one(ID)

        self.assertEqual(row['name'], NAME)

    def test_4_update_category(self):
        ID = 1
        NAME = "GOVERNMENTS"

        self.assertTrue(Category().update(ID, name=NAME))
        self.assertEqual(Category().read().one(ID)['name'], NAME)

    def test_5_delete_category(self):
        ID = 1

        self.assertTrue(Category().delete(ID))
        self.assertFalse(Category().delete(ID))


if __name__ == "__main__":
    unittest.main()
