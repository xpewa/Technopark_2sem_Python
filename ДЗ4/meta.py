from collections.abc import MutableMapping

BEFORE_NAME = "custom_"


class UseDict(MutableMapping):
    """ Additional for CustomMeta class """
    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)

    def __setitem__(self, key, value):
        if key.startswith("__") or key.startswith(BEFORE_NAME):
            self._d[key] = value
        else:
            self._d[BEFORE_NAME + key] = value

    def __setattr__(self, key, value):
        if key.startswith("__") or key.startswith(BEFORE_NAME) or key == "_d":
            return MutableMapping.__setattr__(self, key, value)

        return MutableMapping.__setattr__(self, BEFORE_NAME + key, value)

    def __getitem__(self, key):
        return self._d[key]

    def __delitem__(self, key):
        del self._d[key]

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)


class CustomMeta(type):
    """ Changing the name of the attributes """
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        meta_dict = UseDict()
        meta_dict["__setattr__"] = UseDict.__setattr__
        return meta_dict

    def __new__(cls, name, bases, attrs):
        custom_attr = {
            attr
            if attr.startswith("__") or attr.startswith(BEFORE_NAME)
            else
            BEFORE_NAME + attr: value
            for attr, value in attrs.items()
        }

        return super().__new__(cls, name, bases, custom_attr)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class CustomClass(metaclass=CustomMeta):
    """ Test class """
    x = 50
    custom_iii = "custom_iii"

    def __init__(self, val, data=100):
        self.val = val
        self.data = data

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


if __name__ == '__main__':

    inst = CustomClass(33)
    print(inst.custom_x)
    print(inst.custom_val)
    print(inst.custom_line())
    print(CustomClass.custom_x)
    print(inst.custom_iii)
    print(str(inst) == "Custom_by_metaclass")

    inst.dynamic = "added later"
    print(inst.custom_dynamic == "added later")

#    inst.x  # ошибка
#    inst.val  # ошибка
#    inst.line() # ошибка
#    inst.yyy  # ошибка
#    CustomClass.x  # ошибка
