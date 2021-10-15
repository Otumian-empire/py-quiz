import unittest
from routers import CategoryRouter, QuizRouter, MainRouter
import os


class RouterTest(unittest.TestCase):

    def setUp(self) -> None:
        os.system("make populate")

    def test_1(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
