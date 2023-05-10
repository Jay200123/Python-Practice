# val1 = float(input("Enter a Number: "))
# val2 = float(input("Enter A Second Number: "))
# operator = input("Put an Operator: ")

# if operator == '+':
#     total1 = val1 + val2
#     print("Total:",total1)
# elif operator == '-':
#     total2 = val1 - val2
#     print("Total:", total2)
# elif operator=='/':
#     total3 = val1 / val2
#     print("Total:",total3)
# elif operator=='*':
#     total4= val1 * val2
#     print("Total:",total4)
# else:
#     print("Invalid Operator")
    
print("Advance Calculator Using Functions")
val1 = float(input("Enter a Number: "))
val2 = float(input("Enter A Second Number: "))
operator = input("Put an Operator: ")

def add(value1, value2):
    total = value1 + value2
    return total

def minus(value1, value2):
    total = value1 - value2
    return total

def multiplication(value1, value2):
    total = value1 * value2
    return total  

def division(value1, value2):
    total = value1 / value2
    return total 


if operator == '+':
    addition = add(val1, val2)
    print("Total",  addition)

elif operator == '-':
    subtract = minus(val1, val2)
    print("Total:", subtract)  
    
elif operator == '*':
    multiply = multiplication(val1, val2)
    print("Total:", multiply)

elif operator == '/':
    divide = division(val1, val2)
    print("Total:", divide)

else:
    print("Error Invalid Operator")
    
    

    