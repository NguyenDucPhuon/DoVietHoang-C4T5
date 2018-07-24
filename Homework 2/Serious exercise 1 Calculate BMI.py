height = float(input("Your height in cm ?"))
mass = float(input("Your mass in kg ?"))

BMI = mass / height / height * 10000
print(f"So your BMI is {BMI} ")

if BMI < 16:
    print("You are severely underweight !!")
if 16 <= BMI < 18.5:
    print("You are underweight.")
if 18.5 <= BMI < 25:
    print("You are normal")
if 25 <= BMI < 30:
    print("You are overweight.")
if 30 <= BMI:
    print("You are obese !!")
