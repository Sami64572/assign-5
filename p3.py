class AttributeValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Custom attribute validation logic goes here
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, int) and attr_value < 0:
                raise ValueError(f"Attribute '{attr_name}' must be a non-negative integer.")
            elif isinstance(attr_value, str) and len(attr_value) < 3:
                raise ValueError(f"Attribute '{attr_name}' must be a string with length at least 3.")

        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AttributeValidationMeta):
    x = 5
    name = "John Doe"

if __name__ == "__main__":
    try:
        obj = MyClass(x=-2, name="Jo")
    except ValueError as e:
        print(f"Error: {e}")
