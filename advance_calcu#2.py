print("Python Calculator")
print("Operators: + addition, - minus, / division, * multiplication")
operator = input("Select an Operator: ").lower()

if operator == 'addition' or operator == '+':
    print("(+)Addition")
    num1 = float(input("Enter a Number: "))
    num2 = float(input("Enter a Second Number: "))
    
    def addition(number1, number2):
        total = number1 + number2
        return total
    
    result = addition(num1, num2)
    print("Result:",result)
    
elif operator == 'minus' or operator == '-':
    print("(-)Subtraction")
    num1 = float(input("Enter A Number: "))
    num2 = float(input("Enter A Second Number: "))
    
    def minus(number1, number2):
        total = number1 - number2
        return total
    
    result = minus(num1, num2)
    print("Result:", result)
    
elif operator == 'division' or operator == '/':
    print("(/)Division")
    val1 = float(input("Enter a Value: "))
    val2 = float(input("Enter a Second Value: "))
    
    def divide(value1, value2):
        total = value1 / value2
        return total
    
    result = divide(val1, val2)
    print("Result:", result)
    
elif operator == 'multiplication' or operator == '*':
    print("(*)Multiplication")
    val1 = float(input("Enter a Value: "))
    val2 = float(input("Enter a Second Value: "))
    
    def multiply(value1, value2):
        total = value1 * value2
        return total
    
    result = multiply(val1, val2)
    print("Result:", result)

else:
    print("Invalid Operator...")