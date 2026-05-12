# =========================================
#      STEP / HIKE CALORIE CALCULATOR
# =========================================
# Python 101 Practice Project
# =========================================

print("=" * 50)
print("        STEP / HIKE CALORIE CALCULATOR")
print("=" * 50)

# -------------------------------
# USER INPUT
# -------------------------------

name = input("Enter your name: ")
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))

weight = float(input("Enter your weight in pounds: "))
height_feet = int(input("Enter your height - feet: "))
height_inches = int(input("Enter your height - extra inches: "))

miles = float(input("How many miles did you walk or hike? "))

# -------------------------------
# HEIGHT CONVERSION
# -------------------------------

total_inches = (height_feet * 12) + height_inches

# -------------------------------
# BMI CALCULATION
# BMI = weight / height² * 703
# -------------------------------

bmi = (weight / (total_inches ** 2)) * 703

# -------------------------------
# ESTIMATED STEPS
# Average: about 2,000 steps per mile
# -------------------------------

steps = miles * 2000

# -------------------------------
# CALORIES BURNED ESTIMATE
# Simple walking estimate:
# calories burned = weight * miles * 0.53
# -------------------------------

calories_burned = weight * miles * 0.53

# -------------------------------
# BMI CATEGORY
# -------------------------------

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal weight"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

# -------------------------------
# RESULTS
# -------------------------------

print()
print("=" * 50)
print("              WALK / HIKE REPORT")
print("=" * 50)

print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Weight: {weight:.1f} lbs")
print(f"Height: {height_feet}'{height_inches}\"")

print("-" * 50)

print(f"BMI: {bmi:.2f}")
print(f"BMI Category: {bmi_category}")

print("-" * 50)

print(f"Miles Walked/Hiked: {miles:.2f}")
print(f"Estimated Steps: {steps:.0f}")
print(f"Estimated Calories Burned: {calories_burned:.2f}")

print("=" * 50)

# -------------------------------
# ENCOURAGEMENT MESSAGE
# -------------------------------

if miles >= 10:
    print("Beast mode. That was a serious hike.")
elif miles >= 5:
    print("Great job. That is a strong walk/hike.")
elif miles >= 1:
    print("Nice work. Every mile counts.")
else:
    print("Good start. Keep stacking steps.")

print("=" * 50)
