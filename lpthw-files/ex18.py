def print_two(*args):
    args1, args2 = args
    print(f"args1: {args1}, args2: {args2}")

def print_two_again(args1, args2):
    print(f"args1: {args1}, args2: {args2}")

def print_one(args1):
    print(f"args1: {args1}")

def print_none():
    print("I got nothing.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
