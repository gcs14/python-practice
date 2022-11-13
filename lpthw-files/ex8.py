# Store four customizable slots for the string stored as 'formatter'
formatter = "{} {} {} {}"

# Print formatter with ints inserted
print(formatter.format(1, 2, 3, 4))
# Print formatter with words inserted
print(formatter.format("one", "two", "three", "four"))
# Print formatter with booleans inserted
print(formatter.format(True, False, False, True))
# Print formatter with other formatters inserted
print(formatter.format(formatter, formatter, formatter, formatter))
# Print formatter with strings inserted
print(formatter.format("Try your", "Own text", "Maybe a poem", "Or a song about fear"))
