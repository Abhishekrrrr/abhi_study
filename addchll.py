class hospital:
      def __init__(self,doc,sister,admin,dep):
          self.doc=doc
          self.sister=sister
          self.admin=admin
          self.dep=dep
      def get(self):
          self.doc=input("docter name")
          self.sister=input("sister name")
          self.dep=input("dep?")

class deprt(hospital):
         def print(self):
             print(self.doc, self.sister, self.dep)
class patient(deprt):
    def __init__(s,name,age,diseas):
        s.name=name
        s.age=age
        s.diseas=diseas
    def gg(s):
        s.name=input("enter the patient name")
        s.age=int(input("enter your age"))
        s.diseas=input("your diseas")
    def prt(s):
        print(s.diseas,s.name,s.age)
obj=patient('','','')
obj.get()
obj.print()
obj.gg()
obj.prt()






