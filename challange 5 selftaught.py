a = input("your name")
b= input ("your father name")
a = str(a)
b= str(b)

with open("challange5.txt.txt","w") as challange5:
    challange5.write(a)
    challange5.write(b)
