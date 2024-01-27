class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    obj1 = SingletonClass(42)
    obj2 = SingletonClass(123)

    print(obj1 is obj2)  
    print(obj1.value)    
    print(obj2.value)    
