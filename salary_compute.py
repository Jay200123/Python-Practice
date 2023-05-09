print("Calculating Salary & Wage")

rates = float(input("Enter Rate per Work Hours: "))
hours = int(input("Enter Working Hours: "))
months = input("Enter A Month: ")

if months == 'January':
    days = 31
elif months == 'February':
    days = 28
elif months == 'March':
    days = 31
elif months == 'April':
    days = 30
elif months == 'May':
    days = 31
else:
    print("Enter A Valid Month")
    
def daily(rate, hour):
    
    total = rate * hour
    
    return total

res_daily = daily(rates, hours)
print("Daily Wage:",res_daily)

def weekly(rate, hour):
    
    total = rate * hour * 6
    
    return total 

res_week = weekly(rates, hours)
print("Wage per Week:", round(res_week))

def salary(rate, hour, day):
    
    total = rate * hour * day
    
    return total

res_salary = salary(rates, hours, days)
print("Monthly Salary:", round(res_salary))

def yearly(salary):
    
    total = salary * 12
    
    return total

res_yearly = yearly(res_salary)
print("Salary per Year:",round(res_yearly))