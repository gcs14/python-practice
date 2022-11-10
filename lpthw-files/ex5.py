name  = 'Zed A. Shaw'
age = 35
height = 74 # inches
height_in_cm = height * 2.54
weight = 180 # lbs
weight_in_kg = round(weight * 0.453592, 2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total  = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"\nHeight in centimeters is {height_in_cm} and weight in kilograms is {weight_in_kg}.")
