def Search(answer, word):
    for i in range(0,5):
        if word[i] in answer: 
            if word.find(word[i]) == answer.find(word[i]):
                print(word[i] + ": Exsist at Same Index")
            else:
                print(word[i] + ": Exist at Different Index")
        else:
            print(word[i] + ": Does not Exist")


answer = "MARCH"
Search(answer, "APRIL")
