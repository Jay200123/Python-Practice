print("Calculating Monthly Wage")
rate_Hrs = float(input("Enter Rate Per Hours: "))
work_Hrs = int(input("Enter Work Hours: "))
dayOffs = int(input("Enter Numbers of DayOff: "))
month = input("Enter A Month: ")

if month=='January':
    monthDays = 31
    
elif month == 'February':
    monthDays = 28
    
elif month == 'March':
    monthDays = 31

elif month=='April':
    monthDays = 30
    
elif month=='May':
    monthDays = 31  
      
else:
    print("Enter a Valid Month")    
    
    
daily_Wage = rate_Hrs * work_Hrs
deductions = dayOffs * daily_Wage
monthly_Wage = daily_Wage * monthDays
salary = monthly_Wage - deductions


print("Salary Report for the Month of ", month)
print("Number of Days For Month of", month,":", monthDays,"Days")
print("Number of DayOffs:", dayOffs)
print("Daily Wage:", daily_Wage)
print("Monthly Wage without Deductions:", round(monthly_Wage))
print("Salary Deductions:",deductions)
print("Overall Total Salary:", round(salary))

