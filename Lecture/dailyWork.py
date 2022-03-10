#3/10
print("Input: ")
a = int(input())

for i in range(2,a+1):
    b=0
    if a==2:
        print(a," ")
    for j in range(2,a):
        if i%j==0:
            b=1
    if b==0:
        print(i," ")
