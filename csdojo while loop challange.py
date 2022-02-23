my_list=[9,8,7,6,5,4,3,2,1,-2,-3,-5,-6,-7,-8]
total = 0
i = len(my_list) -1
while my_list[i]<0:
    total+=my_list[i]
    i-=1
print(total)
