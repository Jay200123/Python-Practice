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
    
print("Advance Python Calculator")

val1 = float(input("Put A Value: "))
val2 = float(input("Put A Second Value: "))
op = input("Enter an Operator: ")

def add(num1, num2):
    total = num1 + num2
    return total

def minus(num1, num2):
    total = num1 - num2
    return total

def divide(num1, num2):
    total = num1 / num2
    return total

def multiply(num1, num2):
    total = num1 * num2
    return total

if op == '+':
    addition = add(val1, val2)
    print("result using addition:",addition)
    
elif op == '-':
    subtract = minus(val1, val2)
    print("result using substraction:", subtract)
    
elif op == '/':
    division = divide(val1, val2)
    print("result using division:", division) 
    
elif op == '*':
    multiplication = multiply(val1, val2)
    print("result using multiplication:", multiplication)   
    

    