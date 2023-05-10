print("Computes a Salary")

rates = float(input("Enter Rates per Work Hours: "))
hours = float(input("Enter Work Hours: "))
month = input("Enter A Month: ").lower()
type = input("Type of Wage: ").lower()

if month == 'january':
    days = 31
elif month == 'february':
    days = 28
elif month =='march':
    days = 31
elif month == 'april':
    days = 30
elif month == 'may':
    days = 31
else:
    print("Invalid Month")
    

def daily(rate, hour):
    total = rate * hour
    return total

def weekly(rate, hour):
    total = rate * hour * 6
    return total

def monthly(rate, hour, day):
    total = rate * hour * day
    return total

if type == 'daily':
    dailyWage = daily(rates, hours)
    print("Your Daily Wage:", dailyWage)
    
elif type == 'weekly':
    weeklyWage = weekly(rates, hours)
    print("Your Wage Every Week:", weeklyWage)
    
elif type == 'monthly':
    monthWage = monthly(rates, hours, days)
    print("Your Monthly Wage:", monthWage)

