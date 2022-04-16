from collections import UserList


class CustomList(UserList):

    @staticmethod
    def fill_zero(list1, list2):
        """ Дополняет нулями меньший список до равной длины """
        while(len(list1) < len(list2)):
            list1.append(0)
        while(len(list2) < len(list1)):
            list2.append(0)

    def __add__(self, other):
        list1 = list(self)
        list2 = list(other)
        self.fill_zero(list1, list2)
        new_list = CustomList()
        for item1, item2 in zip(list1, list2):
            new_list.append(item1+item2)
        return new_list

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        list1 = list(self)
        list2 = list(other)
        self.fill_zero(list1, list2)
        new_list = CustomList()
        for item1, item2 in zip(list1, list2):
            new_list.append(item1-item2)
        return new_list

    def __rsub__(self, other):
        list1 = list(other)
        list2 = list(self)
        self.fill_zero(list1, list2)
        new_list = CustomList()
        for item1, item2 in zip(list1, list2):
            new_list.append(item1-item2)
        return new_list

    def __lt__(self, other):
        return (sum(self) < sum(other))

    def __eq__(self, other):
        return (sum(self) == sum(other))

    def __ne__(self, other):
        return (sum(self) != sum(other))

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return (sum(self) >= sum(other))

    def __le__(self, other):
        return (sum(self) <= sum(other))

    def __str__(self):
        return f"list items : {self.data} \n"\
                f"total sum : {sum(self)}"

