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

print("Computes the Daily and Weekly Grosspay")

hourly_Rate = float(input("Enter rate per hour: "))
work_Hours = int(input("Enter Working Hours: "))
weekly = int(input("Enter Number of Days (Work per Week): "))

dailyWage = hourly_Rate * work_Hours
weeklyWage = dailyWage * weekly

print("Daily Wage:", dailyWage)
print("Wage per Week:", round(weeklyWage))