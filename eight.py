#python weight converter\
weight = float(input("Enter your weight: "))
unit = input("Enter the unit (K or L): ")

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.20462
    unit = "Kgs."
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

print(f"your weight is: {round(weight)} {unit}")
