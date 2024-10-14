class grandparent:
    def gdisplay(self):
        print("Grand Parent")
class parent(grandparent):
    def pdisplay(self):
        print("Parent")
class child(parent):
    def cdisplay(self):
        print("child")
c=child()
c.gdisplay()
c.pdisplay()
c.cdisplay()
