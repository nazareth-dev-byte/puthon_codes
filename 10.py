# python compound interest calculator
import math

principal = 0
interest = 0
time = 0




while principal <= 0:
    principal = int(input("Enter the principal amount in $: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")

while interest <= 0:
    interest = int(input("Enter the interest rate: "))
    if interest <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

print(f"Principal: {principal}")
print(f"Interest Rate: {interest}")
print(f"Time: {time}")

amount = principal * (pow(1 + (interest/100), time))
print(f"Balance after {time} years: ${amount:.2f}")
