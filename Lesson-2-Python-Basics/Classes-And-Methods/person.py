class Person:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    # Use `self` in the function arguments so you can use the values
    def persons_info(self):
        print(self.name)
        print(self.age)
        print(self.state)

# Initiate the class
person = Person("John", 40, 'NJ')

# Use a function from the class
person.persons_info()
