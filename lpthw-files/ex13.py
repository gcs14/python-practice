from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called", script)
print("Your first varible is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

plan = input("What do you plan to do with this stuff? ")
print(f"You said you plan to {plan} with this stuff.")
