grades = [95, 67, 83, 45, 70, 58, 100, 77, 89, 92]

pf = ['Pass' if i >= 50 else 'Fail' for i in grades]
gr = ['A' if i >= 90 else 'B' if i >= 80 and i <= 89 else 'C' if i >= 70 and i <= 79 else 'D' if i >= 60 and i <= 69 else 'F' for i in grades ]
total_pass = len([i for i in grades if i >= 50])
avg = sum(grades) / len(grades)
print(pf)
print(gr)
print(total_pass)
print(avg)

