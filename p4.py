class InheritanceRuleMeta(type):
    def __new__(cls, name, bases, dct):
        # Check for the presence of 'common_attribute' in all parent classes
        for base in bases:
            if 'common_attribute' not in dir(base):
                raise TypeError(f"{base.__name__} is missing the 'common_attribute' attribute.")

        # Check for the presence of 'common_attribute' in the current class
        if 'common_attribute' not in dct:
            raise TypeError(f"{name} must have the 'common_attribute' attribute.")

        return super().__new__(cls, name, bases, dct)

class ParentClassA:
    common_attribute = 'Attribute from ParentClassA'

class ParentClassB:
    common_attribute = 'Attribute from ParentClassB'

class ChildClass(InheritanceRuleMeta, ParentClassA, ParentClassB):
    common_attribute = 'Attribute from ChildClass'

if __name__ == "__main__":
    # Creating an instance of ChildClass
    obj = ChildClass()

    # Accessing the 'common_attribute' from ChildClass
    print(obj.common_attribute)