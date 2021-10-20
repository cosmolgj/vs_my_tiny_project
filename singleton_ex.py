class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called.\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called.\n")
            self.data = data
            cls._init = True


s1 = Singleton(3)
s2 = Singleton(4)
print(s1.data)
print(s2.data)
