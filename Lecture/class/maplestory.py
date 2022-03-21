def character():
    name = "타락파워전사"
    STR = 4
    DEX = 4
    INT = 4
    LUK = 4
    gender = "남자"
    hair = "남자 더벅 머리"
    weapon = "검"

def character2():
    name = "아시안느"
    STR = 4
    DEX = 7
    INT = 4
    LUK = 4
    gender = "여자"
    hair = "여자 더벅 머리"
    weapon = "몽둥이"

class Character:
    def __init__(self, name, gender, hair, weapon):
        self.name = name
        self.gender = gender
        self.hair = hair
        self.weapon = weapon
        self.STR = 4
        self.DEX = 4
        self.INT = 4
        self.LUK = 4
    def createCharacter(self):
        print(self.name + "님 축하합니다 캐릭터 생성이 완료 되었습니다") 

    def getStat(self):
        print(self.STR, self.DEX, self.INT, self.LUK)


tarakPowerJunsa = Character("tarakPowerJunsa", "남자", "더벅머리", "검")
asiane = Character("asiane", "여자", "더벅머리", "몽둥이")
zizonPower = Character("zizonPower", "남자", "더벅머리", "창")
bezzy = Character("bezzy", "남자", "머머리", "검")

tarakPowerJunsa.createCharacter()
tarakPowerJunsa.getStat()


if __name__ == "__main__":
    print("메이플스토리를 시작합니다")