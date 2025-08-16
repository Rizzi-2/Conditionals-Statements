number = float(input('Enter a Number: '))
if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is zero (Neutral)")


score = float(input('Enter Your Score from your Exam: '))

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B+"
elif score >= 60:
    grade = "B"
else:
    grade = "F"

print(f"Your Grade is {grade}")

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

#Ternary Operator

even_odd = f"{num} is an Odd Number" if num%2==1 else f"{num} is an Even Number"

print(even_odd)