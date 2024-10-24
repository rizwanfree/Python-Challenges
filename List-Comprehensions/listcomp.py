numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 21, 'grade': 'B'},
    {'name': 'Charlie', 'age': 19, 'grade': 'C'},
    {'name': 'David', 'age': 22, 'grade': 'A'},
    {'name': 'Eve', 'age': 20, 'grade': 'B'}
]

coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]


# result = [i * 2 for i in fruits]

# result = [i.capitalize() for i in fruits]

def time_five(num):
    return num * 5

# result = [time_five(i) for i in numbers]

# square = [i * i for i in numbers]

# even = [i for i in numbers if i % 2 == 0]

# odds = [i for i in numbers if i % 2 == 1]

# doubles = [i * 2 for i in numbers]

# snumbers = [str(i) for i in numbers]

# print(snumbers)

tuples = [tuple((i, i * i)) for i in numbers]

cumulatives = [sum(numbers[:i + 1]) for i in range(len(numbers))]

print(cumulatives)