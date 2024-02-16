# 2798. Number of Employees Who Met the Target
hours = [5,1,4,2,2]
target = 6
employees = []
for i in hours:
    if i >= target:
        employees.append(i)

print(len(employees))

#another way 

employees = 0
for i in hours:
    if i >= target:
        employees += 1

print(employees)