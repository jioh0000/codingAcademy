import random
random.random()

def Search(answer, userInput):
    output = ""
    for char in userInput:
        if char in answer: 
            if userInput.find(char) == answer.find(char):
                output += f"[{char}] "
            else:
                output += f"({char}) "
        else:
            output += f"{char} "
    
    print(output)



wordList = ["THEIR, MARCH"]
answer = wordList[random.randrange(0,2)]

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
    


