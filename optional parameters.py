def f(x=10):
   if x==10:
        print ("x is ten")
   else:
        print("x is not ten")
   default=f()
pass_in=f(2)
print(default)
print(pass_in)
