class father:
    def fdisplay(self):
        print("Father")
class mother:
    def mdisplay(self):
        print("Mother")
class child(father,mother):
    def cdisplay(self):
        print("Child")
c=child()
c.fdisplay()
c.mdisplay()
c.cdisplay()
#in java there is no multiple inheritance we perform this multiple inheritance using interface..

