# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(list, number):
  new_array = []
  for number_in_array in list:
    number_in_array *= number
    new_array.append(number_in_array)
  return new_array

print(multiply_by([10,20,30], 3))
