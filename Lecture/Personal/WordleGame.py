import random
random.random()

def Search(answer, userInput):
    output = ""
    
    for i in range(0,5):
        if userInput[i] == answer[i]:
            output += f"[{userInput[i]}] "
        elif userInput[i] in answer:
            output += f"({userInput[i]}) "
        else:
            output += f"{userInput[i]} "
    
    print(output)



wordList = ["THEIR"]
answer = random.choice(wordList)

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
    


