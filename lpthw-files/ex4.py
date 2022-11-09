# Amount of cars in the fleet
cars = 100
# Space available in each car
space_in_a_car = 4
# Number of drivers on the payroll
drivers = 30
# Number of passengers needed to trasport today
passengers = 90
# Number of unused cars still available
cars_not_driven = cars - drivers
#  Number of cars in use
cars_driven = drivers
# Amount pf people that fit in all the cars evenly
carpool_capacity = cars_driven * space_in_a_car
# Number of people that need to fit in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
