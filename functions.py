from math  import *

input1 = input("Enter Your Name: ")
input2 = input("Enter Your Age: ")

def sayHello(name, age):
    print("Hello there!", name, "You are", age)
    
sayHello(input1, input2)

print("Computes Daily Wage")
workRates = float(input("Enter working rates per hours: "))
workHours = int(input("Enter Working Hours: "))

def dailyWage(rate, hours):
    total = rate * hours
    return total

wage = dailyWage(workRates, workHours)
print("Daily Wage:", wage)

print("Computes WeeklyWage")
val1 = float(input("Enter Working Rates per hour: "))
val2 = int(input("Enter Working Hours: "))
val3 = int(input("Enter Number of Work Days per Week: "))

def weeklyWage(rate, hours, week):
    
    total = rate * hours * week
    
    return total

weekWage = weeklyWage(val1, val2, val3)
print("Your Weekly Wage:", weekWage)


kilo = float(input("Enter Your Weight (Kilo): "))

def computePounds(kilos):
    totalPounds = kilos * 2.2
    return totalPounds

pounds = computePounds(kilo)

print("Total Pounds:", pounds)

print("Calculating Area of Rectangle")

input1 = float(input("Enter Length: "))
input2 = float(input("Enter Width: "))

def AreaRectangle(height, width):
    
    area = height * width
    
    return area

rectangle = AreaRectangle(input1, input2)
print("Area of a Rectangle is :", rectangle)


print("Calculating Area of a Triangle")
base1 = int(input("Enter Value for Base: "))
height2 = int(input("Enter Value for Height: "))

def areaTriangle(base, height):
    area = 1/2 * base * height
    return area

triangle = areaTriangle(base1, height2)
print("Area for Triangle:", triangle)

print("Calculating Area of a Circle")
rad1 = float(input("Enter A Radius: "))

def AreaCircle(radius):
    
    circle = radius * pi
    
    return circle

areaCircle = AreaCircle(rad1)
print("Area of a Circle is:", round(areaCircle))

print("Using Pow in python")

x_val = int(input("Enter A Number: "))
y_val = int(input("Enter A Second Number: "))

def Pythonpow(x, y):
    
    total = pow(x,y)
    return total

result = Pythonpow(x_val, y_val)
print("Result:",round(result))

print("SquareRoot in Python")
num = int(input("Enter A Number: "))

def SquareRoot(number):
    
    total = sqrt(number)
    return total

sqrt_res = SquareRoot(num)
print("The Square Root of the Number is:", round(sqrt_res))

    
    