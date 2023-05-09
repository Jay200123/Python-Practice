print("Calculating Salary Per Month")

rate = float(input("Enter Work Rate per Hours: "))
hour = int(input("Enter Working Hours: "))
months = input("Enter A Month: ")

if months == 'January':
    day = 31
elif months == 'February':
    day = 28
elif months == 'March':
    day = 31
elif months == 'April':
    day = 30
elif months == 'May':
    day = 31
else:
    print("Enter A Valid Month...")
    
def dailyWage(rates, hours):
    
    total = rates * hours
    return total

result1 = dailyWage(rate, hour)
print("Daily Wage:",result1)
    
    
def salary(rates, hours, days):
    
    total = rates * hours * days
    return total

result = salary(rate, hour, day)
print("Salary:", round(result))