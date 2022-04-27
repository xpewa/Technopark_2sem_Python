import unittest
from descriptor import Integer, String, PositiveInteger


class TestInteger:
    data = Integer("_data")

    def __init__(self, data):
        self.data = data


class TestString:
    data = String("_data")

    def __init__(self, data):
        self.data = data


class TestPositiveInteger:
    data = PositiveInteger("_data")

    def __init__(self, data):
        self.data = data


class TestDescriptor(unittest.TestCase):

    def test_integer_set_allow(self):
        data = TestInteger(100)
        self.assertEqual(data.data, 100)

    def test_integer_set_allow_string(self):
        data = TestInteger("89")
        self.assertEqual(data.data, 89)

    def test_integer_set_not_allow(self):
        self.assertRaises(TypeError, TestInteger, "string")

    def test_string_set_allow(self):
        data = TestString("hello")
        self.assertEqual(data.data, "hello")

    def test_string_set_not_allow(self):
        self.assertRaises(TypeError, TestString, 700)

    def test_positive_integer_set_allow(self):
        data = TestPositiveInteger(4)
        self.assertEqual(data.data, 4)

    def test_positive_integer_set_not_int(self):
        self.assertRaises(TypeError, TestPositiveInteger, "string")

    def test_positive_integer_set_not_positive(self):
        self.assertRaises(ValueError, TestPositiveInteger, 0)


if __name__ == '__main__':
    unittest.main()
