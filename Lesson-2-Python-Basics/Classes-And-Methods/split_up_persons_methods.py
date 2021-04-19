class Person:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    # Use `self` in the function arguments so you can use the values
    def persons_name(self):
        print(self.name)

    def persons_age(self):
        print(self.age)

    def persons_state(self):
        print(self.state)

# Initiate the class
person = Person("John", 40, 'NJ')

# Use the `persons_state()` function from the class
person.persons_age()
