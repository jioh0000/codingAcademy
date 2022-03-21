f1 = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "w")
data = "Life is too short"
f1.write(data)
f1.close()

f2 = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "r")
line = f2.read()
print(line)
f2.close()


f1 = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "a")
data = "\nyou need java"
f1.write(data)

f1 = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "r")
data = f1.read()
f1.close()

data = data.replace('java', 'python')

f1 = open("/Users/kis/Documents/GitHub/codingAcademy/Lecture/Input_output/Newfile.txt", "w")
f1.write(data)
f1.close()
