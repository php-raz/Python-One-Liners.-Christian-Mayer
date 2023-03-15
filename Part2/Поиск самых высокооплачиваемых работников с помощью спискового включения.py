employees = {'Alise': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121}

top_earners = []
for k, v in employees.items():
    if v >= 100000:
        top_earners.append((k, v))

print(top_earners)
