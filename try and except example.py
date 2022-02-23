a = input ("insert first value")
b = input ("insert second value")
a = int(a)
b = int(b)
try:
    print (a/b)
except ZeroDivisionError:
    print("second value cannot be 0. Please try again")
