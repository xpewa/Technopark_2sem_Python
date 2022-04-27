import unittest
from meta import CustomMeta


class PresetClass(metaclass=CustomMeta):
    x = 50


class PresetCustomClass(metaclass=CustomMeta):
    custom_x = 40


class PositionalClass(metaclass=CustomMeta):
    def __init__(self, x):
        self.x = x


class NamedClass(metaclass=CustomMeta):
    def __init__(self, *args, x=30):
        self.x = x


class FuncClass(metaclass=CustomMeta):
    def func(self):
        return 20

    def custom_f(self):
        return 200


class NewAttrClass(metaclass=CustomMeta):
    x_old = 50


class TestMeta(unittest.TestCase):

    def test_preset_class(self):
        cls = PresetClass()
        self.assertEqual(cls.custom_x, 50)
        self.assertRaises(AttributeError, lambda: cls.x)
        self.assertRaises(AttributeError, lambda: PresetClass.x)

    def test_preset_custom_class(self):
        cls = PresetCustomClass()
        self.assertEqual(cls.custom_x, 40)
        self.assertRaises(AttributeError, lambda: cls.x)
        self.assertRaises(AttributeError, lambda: cls.custom_custom_x)
        self.assertRaises(AttributeError,
                          lambda: PresetCustomClass.x)
        self.assertRaises(AttributeError,
                          lambda: PresetCustomClass.custom_custom_x)

    def test_positional_class(self):
        cls = PositionalClass(10)
        self.assertEqual(cls.custom_x, 10)
        self.assertRaises(AttributeError, lambda: cls.x)
        self.assertRaises(AttributeError, lambda: PositionalClass.x)

    def test_named_class(self):
        cls1 = NamedClass()
        self.assertEqual(cls1.custom_x, 30)
        self.assertRaises(AttributeError, lambda: cls1.x)
        self.assertRaises(AttributeError, lambda: NamedClass.x)

        cls2 = NamedClass(x=10)
        self.assertEqual(cls2.custom_x, 10)
        self.assertRaises(AttributeError, lambda: cls2.x)

    def test_func_class(self):
        cls = FuncClass()
        self.assertEqual(cls.custom_func(), 20)
        self.assertEqual(cls.custom_f(), 200)
        self.assertRaises(AttributeError, lambda: cls.func)
        self.assertRaises(AttributeError, lambda: FuncClass.func)
        self.assertRaises(AttributeError, lambda: cls.custom_custom_f)
        self.assertRaises(AttributeError, lambda: FuncClass.custom_custom_f)

    def test_new_attr_class(self):
        cls = PresetClass()
        cls.new_attr = 10
        self.assertEqual(cls.custom_new_attr, 10)
        self.assertRaises(AttributeError, lambda: cls.new_attr)
        self.assertRaises(AttributeError, lambda: PresetClass.new_attr)

    def test_new_attr_custom_class(self):
        cls = NewAttrClass()
        cls.custom_new_attr = 0
        self.assertEqual(cls.custom_new_attr, 0)
        self.assertRaises(AttributeError,
                          lambda: cls.custom_custom_new_attr)
        self.assertRaises(AttributeError,
                          lambda: PresetClass.custom_custom_new_attr)


if __name__ == '__main__':
    unittest.main()
