import random

class Dice:

    def __init__(self,faces):
        self.dicefaces = faces

    def roll(self):
        return random.randrange(1, self.dicefaces)

sixdie = Dice(6)
twentydie = Dice(20)
twodie = Dice(2)
fourdie = Dice(4)

print (random.randrange(0, 5))
userinput1 = int(input ('Please select a dice to roll.\n 1. Six sided\n 2. Twenty sided \n 3. Two sided\n 4. Four sided\n '))

if userinput1 == 1:
    answer1 = sixdie.roll()
    print(answer1)
if userinput1 == 2:
    answer2 = twentydie.roll()
    print(answer2)
if userinput1 == 3:
    answer3 = twodie.roll()
    print(answer3)
if userinput1 == 4:
    answer3 = fourdie.roll()
    print(answer3)