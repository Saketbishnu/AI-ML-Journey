marks = [99, 89, 100, 65, 92, "abc", 100.99]

print(marks [0:5])

print(marks [5:len(marks)])

print(marks[:]) # Output: [0,1,2,3,4,5,6,7,8,9] (copy of the whole list)

print(len(marks))

#list are mutable
marks[0] = 98
print(marks)