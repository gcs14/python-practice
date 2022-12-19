# INHERITANCE

# There are three ways that the parent and child classes can interact
#     1. Actions on the child imply an action on the parent.
#     2. Actions on the child override the action on the parent.
#     3. Actions on the child alter the action on the parent.

# Implicit Inheritance

# class Parent(object):
#
#     def implicit(self):
#         print("PARENT implicit()")
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()


# Override Explicitly

# class Parent(object):
#     def override(self):
#         print("PARENT override()")
#
# class Child(Parent):
#     def override(self):
#         print("CHILD override()")
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()


# Alter Before or After

class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()


# All three

# class Parent(object):
#     def override(self):
#         print("PARENT override()")
#
#     def implicit(self):
#         print("PARENT implicit()")
#
#     def altered(self):
#         print("PARENT altered()")
#
# class Child(Parent):
#     def override(self):
#         print("CHILD override()")
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = CHILD()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()


# COMPOSITION

class Other(object):
    def override(self):
        print("Other override()")

    def implicit(self):
        print("Other implicit()")

    def altered(self):
        print("Other altered()")


class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
            self.other.altered()
            print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()


# INHERITANCE VS COMPOSITION:

# 1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with it,
# then be prepared to know the class hierarchy and spend time finding where everything is coming
# from.
# 2. Use composition to package code into modules that are used in many different unrelated places
# and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single
# common concept or if you have to because of something you’re using.
