# To find odd number in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(even_numbers)  
# Output: [1, 3, 5, 7, 9]

