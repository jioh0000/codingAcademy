"""
믹서기
-input: 딸기, 우유, 얼음, 설탕
- output; 딸기 쉐이크

함수의 의미: input --> output
함수를 쓰는 이유:
- 반복을 줄이기 위해
- 일목요연하게 보여주기 위해

용어 정리:
- parameter: 매개변수 --> 받을때
- argument: 인자 --> 부를때
- return: 결과값

def 함수명(매개변수):
    <수행 문장 1>
    ...
"""

def mixer(strawberry, milk, ice, sugar): #매개변수를 받는다
    return 'Strawberry Shake'

#mixer('a','b','c','d') #인자를 넘겨준다

def add(a,b):
    return a + b

def minus(a,b):
    print(a-b)

minus(240, 80)

# 매개변수 지정
result = mixer(sugar=1, milk=2, ice=3, strawberry=3980)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,2,3,4,5))

# *args랑 그냥 섞어서 쓸때
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
        result = 0
    elif choice == 'mul': 
        result = 1
        for i in args:
            result *= i
        return result

print(add_mul('mul',5,4,3,2,1,6,7,8))