# kilo = 74
# number = 2.2

# pounds = kilo * number
# kilos = pounds / number
# print('My Total Pounds are:', pounds)

# print('My Total Kilo are:', kilos)

# if isinstance(pounds, int):
#     print('Data is an Integer')
# else:
#     print('Data is not an Integer')
    
# addition = 3 + 3
# print(addition)

# minus = 50 - 25 
# print(minus)

# multiply = 23 * 7
# print(multiply)

# division = 30 / 3
# print(division)

# total = addition - minus * multiply / division
# print(total)

dailyWage = 590
days = 30
dayOff = 4
workingHrs = 8


offHours = dayOff * workingHrs

totalHours = workingHrs * days - offHours

totalWage = dailyWage * days
 
Deduction = dayOff * dailyWage

Salary = totalWage - Deduction
print('Minimum Wage:', dailyWage)
print('TotalDays:', days)
print('Numbers of DayOff:', dayOff)
print('Number of Working Hours', totalHours)
print('Your Off Hours', offHours)
print('Your Monthly Total Wage is:', totalWage)
print('Your Deductions is:', Deduction)
print('Your Total Salary is:',Salary) 

