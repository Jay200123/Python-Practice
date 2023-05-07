# full_Name = input("Enter Your Full Name:")
# phone = input("Enter Your Phone Number:")
# address = input("Enter Your Address:")
# course = input("Enter Your Course:")
# section = input("Enter Your Section:")
# school_Name = input("Enter Your School Name:")

# print("Your Full Name:", full_Name)
# print("Your Contact Number:", phone)
# print("Your Address:", address)
# print("Your Course:", course)
# print("Your Section:", section)
# print("Your School:", school_Name)



# kilo = input("Enter Kilo: ")
# number = 2.2

# pounds = int(kilo) * float(number)
# print("Pounds is:", pounds)

# print("Performing Addition")
# num1  = input("Enter A Number: ")
# num2 = input("Enter a Second Number: ")

# result = int(num1) + int(num2)

# print("Result:",result)

# print("Find the Area of a Rectangle")

# length = input("Enter the Length: ")
# width = input("Enter the Width: ")

# rectangle = int(length) * int(width)
# print("The Area of the Rectangle is:", rectangle)

# hourly_Rate = float(input("Enter the Minimum Wage Rate: "))
# hours_Work = float(input("Enter Hours Work: "))

# wage = hourly_Rate * hours_Work

# print("Total Wage is:", wage)

min_Wage = float(input("Enter Minimum Wage: "))
month = 31
dayOffs = float(input("Enter Number of Day Off: "))


deduction = dayOffs * min_Wage
totalWage =  min_Wage * month 

salary = totalWage - deduction
print("Total Monthly Wage:", totalWage)
print("Deductions:", deduction)
print("Salary:", salary)
