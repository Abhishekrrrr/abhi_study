file=open("demo.txt",'w')
file.write("hello how are you")
file.close()

file=open("demo.txt",'r')
re=file.read()
print(re)
file.close()

file=open("demo.txt",'a')
file.write("\n iam fine")
file.close()



