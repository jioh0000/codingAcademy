"""

String, 문자열이란, 단어등으로 구성된 문자들의 집합

"Life is too short, You need Python"
"a"
"1234"
"Python is fun"

"""

#문자열에 작은 따음표 포함시키기

food = 'Python\'s favorite food is perl'
food = "Python's favorite food is perl"

# 여러 줄인 문자열을 변수에 대입하고 싶을때
multiline = "Life is too short\n You need python"
print(multiline)

#연속된 작은따음표 3개를 이용하여 multiline 만들기
multiline = '''Life is too short
you need python.'''
print(multiline)

# Concatenation (문자열 합치기)
head = "Jioh is"
tail = " handsome"
print(head + tail)

#문자열 곱하기
a = "Jioh"
print(a*15)

#곱하기 응용
print("="*15)
print("welcome to chess game")
print("press 's' to Start")
print("="*15)

#문자열 길이 구하기
a = "Welcome to Chess Game. This is for you."
print(len(a))

#문자열의 인덱싱과 슬라이싱
"""
인덱싱 --> 무언가를 가르킬수 있는 장소
슬라이스 --> 무언가를 "잘라낸다"
"""

a = "Welcome to Chess Game. This is for you."
print(a[0]) #W
print(a[1]) #e
print(a[-1]) #.
print(a[-2]) #u
print(a[-0]) #W

print(a[0:5]) #Welco
print(a[4:4]) #
print(a[:]) #All

#Replacement
local = "서울동시흥동" 
new_local = local[:2] + '시', local[3:]
print(local, new_local)

"현재 온도는 18도 입니다"
"현재 온도는 20도 입니다"
#문자열의 대임 (Formatting)
degree = 30
print("현재 온도는 %d 입니다" %degree)

#Format 함수를 이용한 포매팅
print("I eat {number} apples and I love {firstName}{lastName}.".format(number = 32, firstName="IU", lastName = "Kim"))

number = 42
firstName = "Jieun"
lastName = "Kim"
print(f"I eat {number} apples and I love {firstName}{lastName}.")

#특정 문자 개수 세기
stringValue = "Welcome I am Youngho Kim. I like Jieun Lee"

sum=0
for x in range(0,len(stringValue)):
    if stringValue[x]=="e":
        sum+=1
print(sum)

print(stringValue.count('e'))
print(len(stringValue))

#문자의 위치 알려주기 find & index (index를 알고 싶을때)
print(stringValue.find("Welcome")) #첫번째 찾기는 인덱스를 저장한다
a = stringValue.find("e")
print(stringValue[a:])

#문자열 삽입 (join)
print(",".join('ABC'))

# .upper(), .lower()
print(stringValue.upper())

#문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("e", "A"))

#문자열 나누기
a = "단편소설(短篇小設)은 일반적으로 대한민국에서는 200자 원고지 150매 이내의 소설을 말한다. 문학동네에서는 80매 이상 200매 이하를 기준으로 하며, 조금이라면 부족하거나 넘쳐도 크게 신경쓰지 않는다고 한다. 단편소설 공모전의 경우 원고지 70~100매 사이를 요구하기도 한다."
array = a.split()
print(array)

b = "a,b,c,d,e,f,g,h"
array = b.split(",")
print(array)
