def calculate_bmi(weight,height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight / (height ** 2)
    return bmi
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi= calculate_bmi(weight, height)
category = bmi_category(bmi)
print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")