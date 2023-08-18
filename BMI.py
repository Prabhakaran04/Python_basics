Body_weight = eval(input('Enter your body weight in KG: '))
height = eval(input('Enter your height in meter: '))
BMI = Body_weight/(height*height)
print('BMI of your Body Weight is', round(BMI, 2))
if BMI <= 18.5:
    print("You are underweight.")
elif 18.5 < BMI <= 24.9:
    print("Your weight is normal.")
elif 25 < BMI <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
