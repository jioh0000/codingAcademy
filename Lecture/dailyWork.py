#3/10
print("Input: ", end="")
a = int(input())

if a>=2:
        print(2," ",end="")

for i in range(3,a+1):
    b=0
    for j in range(2,i):
        if i%j==0:
            b=1
    if b==0:
        print(i," ",end="")

