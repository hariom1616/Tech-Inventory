class Father:
    def __init__(self):
        print("Father Constructor Called")

    def display(self):
        print("This is the Father class")

class Mother:
    def __init__(self):
        print("Mother Constructor Called")

    def display(self):
        print("This is the Mother class")

class Child(Father, Mother):
    def __init__(self):
        # Call both parent constructors
        Father.__init__(self)
        Mother.__init__(self)
        print("Child Constructor Called")

    def display(self):
        # Override to add unique child display
        print("This is the Child class")

# Creating an instance of the Child class
child_instance = Child()
child_instance.display()  # Child display method
Father.display(child_instance)  # Access Father's display
Mother.display(child_instance)  # Access Mother's display