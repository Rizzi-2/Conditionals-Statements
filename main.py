number = float(input('Enter a Number: '))
if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is zero (Neutral)")


score = float(input('Enter Your Weight (kg): '))

if score >= 45:
    weight = "Healthy"
elif score >= 60:
    weight = "Good"
elif score >= 85:
    weight = "Normal"
elif score >= 100:
    weight = "Average"
elif score >= 120:
    weight = "Unhealthy"
elif score >= 150:
    weight = "Fat"
else:
    weight = "CASEOH!"

print(f"Your Fitness is {weight}") 

#Nested Conditions 

num = float(input('Enter a Number: '))
if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
elif num == 0:
    print("Zero (Neutral)")
else:
    print("Negative Number")
#Ok
#Ternary Operator

even_odd = f"{num} is an Odd Number" if num%2==1 else f"{num} is an Even Number"

print(even_odd)