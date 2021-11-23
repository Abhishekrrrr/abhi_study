ict={}
ch='y'
while ch=='y' or ch=='Y':
    name=input("Enter name of product : ")
    price=int(input("Enter the price of product : "))
    ict[name]=price
    ch=input("Want to add items Y : ")
print(ict)
f=input("product search : ")
for i in ict:
    if i==f:
        print("the price of product  is ",ict[i])