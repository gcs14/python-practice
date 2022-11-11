# Amount of types of people
types_of_people = 10
# Store this statement in a string variable
x = f"There are {types_of_people} types of people."

# Store binary as a string variable
binary = "binary"
# Store don't as a string variable
do_not = "don't"
# Store this statement as a string variabnle
y = f"Those who know {binary} and those who {do_not}."

# Now lets print the two statements with their embedded strings
print(x)
print(y)

# Let's restate that by printing two more statements
# With the previous statements embedded
print(f"I said : {x}")
print(f"I also said: '{y}'")

# Give hilarious a boolean value
hilarious = False
# Setup the joke
joke_evaluation = "Isn't that joke funny?! {}"
# Special print format
print(joke_evaluation.format(hilarious))

# Give 'w' a print statement
w = "This is the left side of..."
# Give 'e' a print statement
e = "a string with a right side."

# Print the concatenated result
print(w + e)
