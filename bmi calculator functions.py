name1 = "Yk"
height_m1 = 2
weight_kg1 = 80
name2 = "Yk bro"
height_m2 = 2.5
weight_kg2 = 1202
name3 = "Yk sis"
height_m3 = 2
weight_kg3 = 50
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print ("BMI:")
    print (bmi)
    if bmi < 25:
        return name + " Not overweight"
    else:
        return name + " Is overwieght"
    
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print (result1)
print (result2)
print (result3)
