from math import *
objects = ['rectangle','triangle','circle']     

print("Shapes:", objects)
while True:
    
    shapes = input("Select a Shape: ")
    
    if shapes == objects[0]:
        print("Calculate Area of Rectangle")
        height = float(input("Enter Height: "))
        width = float(input("Enter Width: "))
        
        def areaRectangle(height, width):
            total = height * width
            return total
        
        result = areaRectangle(height, width)
        print("Area of a Rectangle:", result)
        
    elif shapes == objects[1]:
        print("Area of a Triangle")
        length = float(input("Enter Length: "))
        width = float(input("Enter Width: "))
        
        def areaTriangle(length, width):
            total = 0.05 * length * width
            return total
        
        result = areaTriangle(length, width)
        print("Area of a Triangle:", result)
        
    elif shapes == objects[2]:
        print("Calculates Area of a Circle")
        radius = float(input("Enter Radius: "))
        
        def areaCircle(radius):
            total = radius * pi
            return total
        
        result = areaCircle(radius)
        print("Area of a Circle:", round(result))
        
    else:
        print("Invalid Shape")
        break
        