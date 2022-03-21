#1,3,5,7,9 = elements (요소)
odd = [1,3,5,7,9]

a = []
b = [1,2,3]
c = ["Life", "is", "too", "short"]
d = [1,2,"Life", "is"] #type을 신경쓰지 않는다
e = [1,2, ["Life", "is"]]
f = [1,2,[3,4,[5,6,[7]]]]

#리스트의 슬라이싱
a = [1,2,3,['a','b','c'], 4,5]
print(a[2:5])
print(a[3][0:2])

#리스트 더하기
a = [1,2,3]
b = [9,8,7]
c = a+b
print(c)

#리스트 반복하기
a = [1,2,3]
print(a*30)

#리스트 길이구하기
b = len(a)
print(b)

a = [1,2,3,4,5,6]
a[3] = 5
print(a)

#🔥🔥🔥🔥🔥🔥🔥🔥🔥리스트 관련 함수들🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

#append
ls = [1,4,3,2,7,5]
ls.append(121)
print(ls)

#sort #QUICK SORT
ls.sort()
print(ls)

#reverse
ls.reverse()
print(ls)

#index
print(ls.index(121))

#insert
ls.insert(1, 122)
print(ls)

#remove
ls.remove(122)
print(ls)
del ls[4]
print(ls)

#pop
print("pop")
a = ls.pop(-1)
print(a)

#count
ls = [1,1,1,1,1,1,1,2,2,2]
print(ls.count(1))

#str() 스트링 타입으로 바꾸기
a = ["Life", "is", "too", "short"]
a = str(a)
print(a)
print(type(a))

