#3/10
"""
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
"""

#3/11
"""
a = 0
b = 5
for i in range(0,11):
    for k in range(0,b-i):
        print(" ", end="")
    for j in range(a,i*2+1):
        print("*", end="")
    if i>4: 
        a+=4
        b+=2
    print()
"""

#3/12
"""
a=0
for i in range(0,4):
    for j in range(0,4):
        print(j+i,end=" ")
    print()
"""

#3/13
"""

"""
low_prices = [100,200,400,800,1000]
high_prices = [150,300,430,880,1000]
volatility = []

for i in range(0,len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])

for i in range(0,5):
    print(volatility[i], end=" ")