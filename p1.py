class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class: {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=LoggingMeta):
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    obj = MyClass(42)