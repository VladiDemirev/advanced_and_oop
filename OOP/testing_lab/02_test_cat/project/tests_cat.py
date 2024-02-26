from unittest import TestCase, main

from project.cat import Cat


class CatTests(TestCase):

    def setUp(self):
        self.test_cat = Cat("Shishman")

    def test_initialization(self):
        self.assertEqual("Shishman", self.test_cat.name)
        self.assertFalse(self.test_cat.fed)
        self.assertFalse(self.test_cat.sleepy)
        self.assertEqual(0, self.test_cat.size)

    def test_cat_is_fed_and_sleepy_and_size_increased_when_eaten(self):
        expected_size = self.test_cat.size + 1
        self.test_cat.eat()
        self.assertTrue(self.test_cat.fed)
        self.assertTrue(self.test_cat.sleepy)
        self.assertEqual(expected_size, self.test_cat.size)

    def test_raise_exception_if_cat_is_fed_when_eat_is_called(self):
        self.test_cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.test_cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_not_sleepy_when_slept(self):
        self.test_cat.sleepy = True
        self.test_cat.fed = True
        self.test_cat.sleep()
        self.assertFalse(self.test_cat.sleepy)

    def test_cat_cannot_sleep_when_hungry(self):
        # self.test_cat.fed = False
        # self.test_cat.sleepy = True
        with self.assertRaises(Exception) as ex:
            self.test_cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == "__main__":
    main()
