class Integer:
    """ Checks if the value set is a number """
    def __init__(self, attr):
        self.attr = attr

    def __get__(self, obj, objtype):

        return getattr(obj, self.attr)

    def __set__(self, obj, val):

        if isinstance(val, int):
            setattr(obj, self.attr, val)
        else:
            try:
                value = int(val)
                setattr(obj, self.attr, value)
            except ValueError as not_int:
                raise TypeError(f"Expected {val} to be an int") from not_int


class String:
    """ Checks if the value set is a string """
    def __init__(self, attr):
        self.attr = attr

    def __get__(self, obj, objtype):

        return getattr(obj, self.attr)

    def __set__(self, obj, val):

        if isinstance(val, str):
            setattr(obj, self.attr, val)
        else:
            raise TypeError(f"Expected {val} to be an str")


class PositiveInteger:
    """ Checks if the value set is a positive int """
    integer = Integer("_integer")

    def __init__(self, attr):
        self.attr = attr

    def __get__(self, obj, objtype):

        return getattr(obj, self.attr)

    def __set__(self, obj, val):

        self.integer = val
        if self.integer > 0:
            setattr(obj, self.attr, self.integer)
        else:
            raise ValueError(f"Expected {val} to be an positive int")


class Data:
    """ Test class """
    num = Integer("_num")
    name = String("_name")
    price = PositiveInteger("_price")

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price

    def __str__(self):
        return(f"num={self.num}, name={self.name}, price={self.price}")


if __name__ == '__main__':
    my_data = Data(5, "9", 999)
    print(my_data)
