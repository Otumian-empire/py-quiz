import unittest
from utils import placeholder_update


class UtilsTest(unittest.TestCase):

    def test_empty_keys(self):
        keys = []
        val = ""
        self.assertEqual(placeholder_update(keys), val)

    def test_one_key(self):
        keys = ['full_name', ]
        val = "full_name=?"
        self.assertEqual(placeholder_update(keys), val)

    def test_two_keys(self):
        keys = ['full_name', 'age', ]
        val = "full_name=?, age=?"
        self.assertEqual(placeholder_update(keys), val)

    def test_five_keys(self):
        keys = ['full_name', 'age', 'dob', 'job', 'height']
        val = "full_name=?, age=?, dob=?, job=?, height=?"
        self.assertEqual(placeholder_update(keys), val)

    def test_non_string_keys(self):
        with self.assertRaises(Exception):
            keys = [1, 2, 3]
            placeholder_update(keys)


if __name__ == "__main__":
    unittest.main()
