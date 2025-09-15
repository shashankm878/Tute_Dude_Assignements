# Task 2: Demonstrate List Slicing

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements using slicing
first_five = numbers[:5]

# Reverse the extracted elements
reversed_first_five = first_five[::-1]

# Print both lists
print ("Original List:", numbers)
print("Extracted list:", first_five)
print("Reversed list:", reversed_first_five)