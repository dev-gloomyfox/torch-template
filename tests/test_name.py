import unittest

from app_name.name import run_name


class NameTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, run_name(1), msg="Expect message")


if __name__ == "__main__":
    unittest.main()
