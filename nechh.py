class Computer:

    def __init__(self, ram, gpu, processor):
        self.ram = ram
        self.gpu = gpu
        self.processor = processor

    def getspecs(self):
        print("Enter specifications")
        self.ram = input("Enter RAM size: ")
        self.gpu = input("Enter GPU model: ")
        self.processor = input("Enter PROCESSOR model: ")

    def displayspecs(self):
        print("Specifications of your system")
        print(self.ram, self.gpu, self.processor)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_color(self):
        self.casecolor = input("Enter case color: ")
    def showcolor(self):
        print("Desktop case color")
        print(self.casecolor)


class Laptop(Desktop):
    def __init__(s, weight):
        s.weight = weight

    def get_weight(s):
        s.weight = input("Enter weight: ")

    def show_weight(s):
        print("Laptop weight")
        print(s.weight)


object1 = Laptop(" ")
object1.getspecs()
object1.get_weight()
object1.get_case_color()
object1.showcolor()
object1.displayspecs()
object1.show_weight()