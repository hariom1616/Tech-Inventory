class Overloading:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print("Both parameters:", a, b)
        elif a is not None:
            print("One parameter:", a)
        else:
            print("No parameters")
            
# Create an instance of the class
obj = Overloading()

# Call the display method with varying number of parameters
obj.display()        # No parameters
obj.display(10)      # One parameter
obj.display(10, 20)  # Two parameters