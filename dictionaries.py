monthConversion = {
    "jan":"January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul":"July",
    "aug":"August",
    "sept": "September",
    "oct": "October",
    "nov":"November",
    "dec": "December"
}


while True:
    
    val = input("Enter a Month: ")
    
    if val not in monthConversion:
        print("Invalid please Enter a valid value pair..")
    else:
        print(monthConversion.get(val))
        break