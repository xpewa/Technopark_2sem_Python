import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_fill_zero_first_less(self):
        list1 = [1, 2]
        list2 = [1, 2, 3]
        CustomList.fill_zero(list1, list2)
        self.assertEqual(list1, [1, 2, 0])
        self.assertEqual(list2, [1, 2, 3])

    def test_fill_zero_second_less(self):
        list1 = [1, 2, 3, 4]
        list2 = [1]
        CustomList.fill_zero(list1, list2)
        self.assertEqual(list2, [1, 0, 0, 0])
        self.assertEqual(list1, [1, 2, 3, 4])

    def test_add_custom_and_custom(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([10])
        lst3 = lst1 + lst2
        self.assertEqual(lst3.data, [11, 2, 3])

    def test_add_custom_and_list(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = [4, 5, 6, 7]
        lst3 = lst1 + lst2
        self.assertEqual(lst3.data, [5, 7, 9, 7])

    def test_add_list_and_custom(self):
        lst1 = [0, 5]
        lst2 = CustomList([10, 10, 10, 10, 10])
        lst3 = lst1 + lst2
        self.assertEqual(lst3.data, [10, 15, 10, 10, 10])

    def test_sub_custom_and_custom(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([10])
        lst3 = lst1 - lst2
        self.assertEqual(lst3.data, [-9, 2, 3])

    def test_sub_custom_and_list(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = [4, 5, 6, 7]
        lst3 = lst1 - lst2
        self.assertEqual(lst3.data, [-3, -3, -3, -7])

    def test_sub_list_and_custom(self):
        lst1 = [0, 5]
        lst2 = CustomList([10, 10, 10, 10, 10])
        lst3 = lst1 - lst2
        self.assertEqual(lst3.data, [-10, -5, -10, -10, -10])

    def test_lt(self):
        self.assertTrue(CustomList([10]) < CustomList([100]))

    def test_eq(self):
        self.assertTrue(CustomList([10]) == CustomList([1, 2, 2, 5]))

    def test_ne(self):
        self.assertTrue(CustomList([10]) != CustomList([-10]))

    def test_gt(self):
        self.assertTrue(CustomList([100]) > CustomList([10, 10, 10, 10]))

    def test_ge(self):
        self.assertTrue(CustomList([100]) >= CustomList([20, 20, 20, 20, 20]))

    def test_le(self):
        self.assertTrue(CustomList([100]) <= CustomList([20, 20, 20, 20, 20]))

    def test_str(self):
        lst = CustomList([1, 2, 3])
        self.assertEqual(
            "list items : [1, 2, 3] \n"
            "total sum : 6",
            lst.__str__())


if __name__ == '__main__':
    unittest.main()
