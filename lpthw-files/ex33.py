# i = 0
numbers = []

def add_numbers(max_number):
    i = 0
    while i < max_number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

add_numbers(4)

print("The numbers: ")

for num in numbers:
    print(num)
