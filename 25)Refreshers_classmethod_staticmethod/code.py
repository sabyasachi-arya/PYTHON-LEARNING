class TestClass:
    def instance_method(self):  # instance method gets the object as argument in parameter
        print(f"called instance method of {self}")

    @classmethod  # because it's a class method , it has to be notified that the class is getting used
    # in a class method inside the class itself
    def class_method(cls):  # class method gets the class as the argument in parameter
        print(f"called class_method of {cls}")

    @staticmethod  # these are called decorators
    def static_method():   # static method gets nothing as argument
        print(f"Called static method.")


test = TestClass()  # used for instance method
test.instance_method()
TestClass.class_method()  # used for class method
TestClass.static_method()  # used for static method
