# input의 사용

# 한줄에 결과값 모두 출력하기
# ,end=' '

"""
파일 열기모드
w = 쓰기모드 --> 파일에 내용을 쓸 때 사용
r = 읽기모드 --> 파일을 읽기만 할 때 사용
a = 추가모드 --> 파일의 마지막에 새로운 내용을 추가 시킬때 사용
"""
f = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", 'w') #w = write
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close



f = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "r")
while True:
    line = f.readline().strip()
    if not line: break
    print(line)
f.close



f = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "a")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
