"""
= Hash, Associative array, DIctionary

"이름" = 김영호
"생일" = "몇월 몇일"

people = 사람들
baseball = 야구(key) : (value)
key = value

{Key1:Value1, Key2:Value2, Key3:Value3, ...}
- Key는 변하지 않는 값을 사용
- Value에는 변하는 값과 변하지 않는 값 모두 사용 가능
"""

dic = {'name':'Jioh', 'phone':'01027771209', 'birth':'051201'}
'''
Key | Value
name| Jioh
phone| 01027771209
birth| 051201
'''

a = {1: 'hi'} 
a = {'a': [1,2,3]}

#딕셔너리에 쌍 추가하기
a = {1: 'a'}
a['name'] = 'jioh' # a 딕셔너리에 'name'라는 키의 값을 'jioh'로 설정해라
print(a)
a['apple'] = '맛있다'
print(a)
a['apple'] = '맛없다' #update
a['List'] = [12,2,3,5,6,2]
print(a)

#딕셔너리 요소 삭제하기
del a['apple']
print(a)

#딕셔너리 Key를 이용해서 Value 얻는법
grade = {'Jioh':40, 'Youngho':100, 'Jenny':50, 'Rosie':60}
greatestStudent = grade['Youngho']
print(greatestStudent)

print(list(grade.keys())) #list() 넣고 빼고 가능
print(list(grade.values()))
print(list(grade.items()))

#grade = {} #메모리가 조금 남음
#grade = dict() #메모리가 조금 남음
#grade.clear() #메모리가 남지 않음

if 'Youngho' in grade:
    print(True)

if 'Jisoo' not in grade:
    grade['Jisoo'] = 100
    print(grade)