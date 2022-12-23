import random

lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z']

uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '&', '*', '~', '?']

all_characters = lowercase_letters + uppercase_letters + numbers +special_characters

print("Welcome to Password Generator 9000! Let's begin.")

required_length = int(input("\nHow long do you want your pass word to be? "))
generated_password = []

while len(generated_password) != required_length:
    generated_password.append(random.choice(all_characters))

print("\nYour new password is:", "".join(generated_password))
print("Don't forget it! It'll be a $1000 service fee to retrieve that code if you do.")
