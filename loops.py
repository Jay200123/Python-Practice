print("Calculate Daily Wage:")

while True:
    
    rate = float(input("Enter rate per hours: "))
    hour = float(input("Enter work hours: "))
    
    def dailyWage(rates, hours):
        total = rates * hours
        return total
    
    result = dailyWage(rate, hour)
    print(result)