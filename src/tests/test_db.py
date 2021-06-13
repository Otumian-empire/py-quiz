import unittest
from glob import glob

from set_up import set_up_database_and_tables
from settings import DATABASE


class DBTest(unittest.TestCase):

    def setUp(self) -> None:
        set_up_database_and_tables()

    def test_database_exists(self):
        self.assertTrue(DATABASE in glob("*"))


if __name__ == "__main__":
    unittest.main()
