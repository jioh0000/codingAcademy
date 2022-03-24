
def Search(answer, userInput):
    output = ""
    index = 0
    for char in userInput:
        if char in answer: 
            if index == int(answer.find(char)):
                output += f"[{char}] "
            else:
                output += f"({char}) "
        else:
            output += f"{char} "
    index+=1
    print(output)



answer = "MARCH"

print("<RULE>")
print("[] = A letter insdie is in the answer at same index")
print("() = A letter insdie is in the answer at different index")
print("-----------------------")
print("Game Start")
print("-----------------------")
for chance in range(0,6):
    print("Five Letter Word: ", end="")
    userInput = input().upper()
    Search(answer, userInput)
    


