a = 1
b = "a"
c = "abc"
d = 2.0

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#조건문
a = 3
if a > 1: print("a is greater than 1")

#for
for a in [1,2,3]: print(a)

for i in range(0,5):
    print(i)

#while
i = 0
while i < 3:
    i += 1
    print(i)

#함수
def add(a, b):
    return a + b

print(add(4,5))


for i in range(0,5):
    for j in range(i,5):
        print("*", end="")
    print()
    