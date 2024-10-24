numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

neg_numbers = [10, -1, 0, 5, -3, 6, 0, -7]

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

words = ["hi", "apple", "banana", "cat", "date", "elderberry"]

celsius_temps = [0, 20, 37, 100]

# result = [i if i % 2 == 0 else False for i in numbers]

# words = ['Even' if i % 2 == 0 else 'Odd' for i in numbers]

# size = ['small' if i <= 5 else 'medium' if i > 5 and i <= 8 else 'large' for i in numbers]

# pn = [True if i > 0 else False if i < 0 else 0 for i in neg_numbers]

# square = [ i * i if i > 0 else i for i in neg_numbers]

# lenth = [len(i) for i in fruits]

#flenth = [len(i) for i in words if len(i) > 3]

size = ['small' if len(i) <= 3 else 'medium' if len(i) <= 6 else 'long' for i in words]

convert_to_forenheit = [((i * 9) / 5) + 32 for i in celsius_temps]

square = [i * i for i in numbers if i > 5]

print(square)