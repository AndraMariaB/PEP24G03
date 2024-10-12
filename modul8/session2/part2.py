class Example:
    A = 10
    B = 20
    C = 30

    def change_attr(self, attr=None, val=None):
        if attr is None:
            pass
        elif attr and not val:
            delattr(self, attr)
            # self.__delattr__(attr)
        else:
            print(getattr(self, attr), f"<- value of attribute {attr}")
            # print(self.__getattribute__(attr), f"<- value of attribute {attr}")
            setattr(self, attr, val)
            # self.__setattr__(attr, val)


e = Example()
e.change_attr('A', 5)
print(e.A, "<- value after change")
e.change_attr('A')
print(e.A, "<- value after delete")
