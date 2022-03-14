a = 1
b = "Python"
c = [1,2,3]


temp = [1,2,3,4]
print(id(temp))

b = temp
print(id(b))

print(temp is b)
temp[1] = 5
print(temp, b)