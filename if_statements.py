print("Answer  Yes Or No")
input1 = input("Are you a Men?: ").lower()
input2= input("You like BlackPink?: ").lower()

if input1 == 'yes' and input2 == 'no':
    print("You Are a Men")

elif input1 == 'no' and input2 == 'yes':
    print("You are A Female and Likes BlackPink")
    
elif input1 == 'yes' and input2=='yes':
    print("Your are not Men You are Gay")

elif input1 == 'no' and input2 == 'no':
    print("You are A Female but does not like Kpop")
    
else:
    print("Wrong Answer")

print("Finding the Biggest Number")
    
num1 = int(input("Enter A Number: "))
num2 = int(input("Enter A Second Number: "))
num3 = int(input("Enter a Third Number: "))

def biggestNumber(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
number = biggestNumber(num1, num2, num3)
print("Biggest Number is:", number) 

def lowestNumber(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3
    
low_number = lowestNumber(num1, num2, num3)
print("The Lowest Number are: ", low_number)
