from math  import *

input1 = input("Enter Your Name: ")
input2 = input("Enter Your Age: ")

def sayHello(name, age):
    print("Hello there!", name, "You are", age)
    
sayHello(input1, input2)

workRates = float(input("Enter working rates per hours: "))
workHours = int(input("Enter Working Hours: "))

def dailyWage(rate, hours):
    total = rate * hours
    return total

wage = dailyWage(workRates, workHours)
print("Daily Wage:", wage)

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


print("Calculating Area of a Circle")
rad1 = float(input("Enter A Radius: "))

def AreaCircle(radius):
    
    circle = radius * pi
    
    return circle

areaCircle = AreaCircle(rad1)
print("Area of a Circle is:", round(areaCircle))
    
    

