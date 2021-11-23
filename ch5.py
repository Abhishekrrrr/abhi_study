dic = { }

while True :
    product = input("enter the name of product (enter q for quit )= ")
    if product == "q" or product == "Q" :
        break
    else :
        price = int(input("enter the price of product = "))
        dic [ product ] = price

while True :
    name = input("enter the name of product those you are entered (enter q for quit )= ")
    if name == "q" or name == "Q" :
        break
    else :
        if name not in dic :
            print("name of product is invaild")
        else :
            print("price of product = ",dic[name])