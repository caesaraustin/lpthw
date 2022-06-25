cars=100
space_in_a_car=4.0
#
#depending on the language, there is a promotion scheme where one integer will be "promoted" to be a floating number
# 4.0 * 5 = 20.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven


print("there are", cars, "cars available.")
print("there are only", drivers, "drivers available.")
print("there will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car,")

#using 4 instead of 4.0 doesn't change the final answers but it makes the 120.0 into 120
# = gives data (numbers, strings, etc.) names
#in line 7, car_pool_capacity is named carpool_capacity