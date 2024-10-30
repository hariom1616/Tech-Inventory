class GrandParent:
    def display(self):
        print("Grand Parent")

class Parent(GrandParent):
    def display(self):
        super().display()
        print("Parent")

class Child(Parent):
    def display(self):
        super().display()
        print("Child")

# Create an instance of Child and display the hierarchy
c = Child()
c.display()