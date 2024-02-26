from unittest import TestCase, main

from extended_list import IntegerList


class IntegerListTest(TestCase):
    def setUp(self):
        self.integer_list_empty = IntegerList()
        self.integer_list_only_int_data = IntegerList(1, 2, 3)
        self.integer_list_mixed_data = IntegerList(1, "a", 3)

    def test_initiliazion_empty_list(self):
        self.assertEqual([], self.integer_list_empty.get_data())

    def test_initiliazion_valid_list(self):
        self.assertEqual([1, 3], self.integer_list_mixed_data.get_data())

    def test_add_data_invalid_element(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list_only_int_data.add("b")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_add_data_valid_element(self):
        result = self.integer_list_only_int_data.add(4)
        self.assertEqual([1, 2, 3, 4], result)

    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list_only_int_data.remove_index(10)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_remove_valid_index(self):
        result = self.integer_list_only_int_data.remove_index(1)
        self.assertEqual(2, result)
        self.assertEqual([1, 3], self.integer_list_only_int_data.get_data())

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list_only_int_data.get(10)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_valid_index(self):
        result = self.integer_list_only_int_data.get(1)
        self.assertEqual(2, result)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list_only_int_data.insert(10, 4)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_valid_index_invalid_element(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list_only_int_data.insert(1, "b")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_valid_index_valid_element(self):
        self.integer_list_only_int_data.insert(2, 4)
        result = self.integer_list_only_int_data.get_data()
        self.assertEqual([1, 2, 4, 3], result)

    def test_get_biggest(self):
        result = self.integer_list_only_int_data.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.integer_list_only_int_data.get_index(2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
