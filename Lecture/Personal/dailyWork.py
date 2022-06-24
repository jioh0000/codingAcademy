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
low_prices = [100,200,400,800,1000]
high_prices = [150,300,430,880,1000]
volatility = []

for i in range(0,len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])

for i in range(0,5):
    print(volatility[i], end=" ")
"""

#3/16
"""
Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a, b = map(int,input().split())
day = 0

for x in range(0,a-1):
    day+=Days[x]

day+=b 

if day%7==1: print("MON")
elif day%7==2: print("TUE")
elif day%7==3: print("WED")
elif day%7==4: print("THU")
elif day%7==5: print("FRI")
elif day%7==6: print("SAT")
elif day%7==0: print("SUN")
"""

#3/28
#https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
"""
def solution(arr):
    answer = []
    store = 10
    for a in arr:
        if a != store:
            answer.append(a)
        store = a
    
    return answer
"""

#4/2
#https://programmers.co.kr/learn/courses/30/lessons/12912
'''
def solution(a, b):
    answer = 0
    
    if a<=b:
        for i in range(a,b+1):
            answer+=i
    else:
        for i in range(a,b-1,-1):
            answer+=i
    return answer
'''

#5/15
# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
"""
def solution(new_id):
    answer = ''
    answer = new_id.lower()
    previous = '.'
    
    for letter in answer:
        if not(letter.isalpha()) and not(letter.isdigit()) and not(letter=='-') and not(letter=='_') and not(letter=='.'):
            answer = answer.replace(letter,"")
            
    for letter in answer:
        try:
            if previous=='.' and letter=='.': 
                x = answer.index('.')
                answer = answer[:x] + answer[x+1:]
            previous = letter
        except:
            print(answer)
            pass
    try:
        if answer[0]=='.': answer = answer[1:]
        if answer == '': answer = 'a'

        if len(answer) > 15:
            answer = answer[:15]
            if answer[-1]=='.': answer = answer[:-1]
        if len(answer) < 3:
            while(len(answer)!=3): answer += answer[-1]
    except:
        pass
    
    return answer
"""

"""
def solution(answers):
    answer = []
    count1, count2, count3 = 0,0,0
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    for x in range(0,len(answers)):
        if answers[x] == num1[x%5]:
            count1 += 1
        if answers[x] == num2[x%8]:
            count2 += 1
        if answers[x] == num3[x%10]:
            count3 += 1
            
    if count1 > count2:
        if count1 > count3: answer.append('1')
        else: answer.append('3')
    else:
        if count2 > count3: answer.append('2')
        else: answer.append('3')
    
    return answer

answers = [1,2,3,4,5]

solution(answers)
"""

"""
def solution(left, right):
    answer = 0
    for x in range(left,right+1):
        count = 0
        for i in range(1,x+1):
            if x%i == 0:
                count += 1
        if count%2 == 0:
            answer += x
        else:
            answer -= x
    
    return answer
"""

# 6/24

sum = 0
temp = 0
a = int(input())
b = map(int, input().split())

b = list(b)
b.sort()

for i in b:
    sum += (temp + i)
    temp += i

print(sum)