def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
     return "Under weight"
    elif 18.5 <= bmi < 25:
     return "Normal weight"
    elif 25 <= bmi < 30:
     return "Over Weight"
    else:
     return "obese"

user_action = input(" Hi There!!  ")
weight = float(input("enter your weight in KGs :  "))
height = float(input("enter your height in Metres :  "))
bmi = calculate_bmi(weight, height)
bmi_category = get_bmi_category(bmi)
print(f"Your bmi is: {bmi} ")
print(f"Your bmi is: {bmi_category} ")

