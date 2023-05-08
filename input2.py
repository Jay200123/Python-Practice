print("Calculating Monthly Wage")
rate_Hrs = float(input("Enter Rate Per Hours: "))
work_Hrs = int(input("Enter Work Hours: "))
dayOffs = int(input("Enter Numbers of DayOff: "))

month = 31

daily_Wage = rate_Hrs * work_Hrs
deductions = dayOffs * daily_Wage
monthly_Wage = daily_Wage * month
salary = monthly_Wage - deductions

print("Salary Report")
print("Number of Days For Month of May:", month, "Days")
print("Number of DayOffs:", dayOffs)
print("Daily Wage:", daily_Wage)
print("Monthly Wage without Deductions:", round(monthly_Wage))
print("Salary Deductions:",deductions)
print("Overall Total Salary:", round(salary))