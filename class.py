class student:
      def __init__(self,name,mark):
          self.name=name
          self.mark=mark
      def getdet(self):
          self.name=input("enter your name")
          self.namme=int(input("enter mark"))
      def prt(self):
          print(self.name,self.mark)
obj=student('','')
obj.getdet()
obj.prt()



