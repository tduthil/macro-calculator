# This program calculates the total calories and the macros in grams.

# Prompt the user to provide their gender
gender = input("What is your gender? (M/F): ")

# Prompt the user to provide weight in lbs and height in feet and inches and age
weight = float(input("Enter your weight in lbs: "))
height = input("Enter your height in feet and inches: ")
age = int(input("Enter your age: "))

# Convert the weight to kilograms
weight_kg = weight / 2.20462

# Convert the height to centimeters
height_cm = (height * 12) + (inches * 2.54)

# Calculate the basal metabolic rate (BMR)
BMR = 66.5 + (13.75 * weight_kg) + (5.003 * height_cm) - (6.755 * age)

# Prompt the user to provide their activity level
activity_level = int(input("Enter your activity level (1-4): "))

# Calculate the total calories needed
calories_needed = BMR * activity_level

# Set the default percentages for protein, carbohydrates, and fat
protein_percentage = 40
carbohydrate_percentage = 30
fat_percentage = 30

# Calculate the number of grams of protein needed
protein_grams = (calories_needed * protein_percentage) / 4

# Calculate the number of grams of carbohydrates needed
carbohydrate_grams = (calories_needed * carbohydrate_percentage) / 4

# Calculate the number of grams of fat needed
fat_grams = (calories_needed * fat_percentage) / 9

# Print the results
print("Your total calories needed is: ", calories_needed)
print("Your protein grams needed is: ", protein_grams)
print("Your carbohydrate grams needed is: ", carbohydrate_grams)
print("Your fat grams needed is: ", fat_grams)

# Activity level values:
# 1.2 = Sedentary (little or no exercise)
# 1.375 = Lightly active (light exercise 1-3 days/week)
# 1.55 = Moderately active (moderate exercise 3-5 days/week)
# 1.725 = Very active (hard exercise 6-7 days/week)
