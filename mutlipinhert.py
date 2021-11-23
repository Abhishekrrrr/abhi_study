class student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getdet(self):
        self.name = input("enter your name")
        self.mark = int(input("enter mark"))

    def prt(self):
        print(self.name, self.mark)


class techer(student):
    def dis(self):
        print("ggg")
class admin(techer,student):
    def ss(self):
        print("ff")
obj=admin('','')
obj.getdet()
obj.prt()
obj.dis()
obj.ss()

