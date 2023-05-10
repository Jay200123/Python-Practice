val1 = float(input("Enter a Number: "))
val2 = float(input("Enter A Second Number: "))
operator = input("Put an Operator: ")

if operator == '+':
    total1 = val1 + val2
    print("Total:",total1)
elif operator == '-':
    total2 = val1 - val2
    print("Total:", total2)
elif operator=='/':
    total3 = val1 / val2
    print("Total:",total3)
elif operator=='*':
    total4= val1 * val2
    print("Total:",total4)
else:
    print("Invalid Operator")