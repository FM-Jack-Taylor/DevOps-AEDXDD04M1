class Lettercheck:

    def vowelscheck(input):
        if input in vowels:
            return True
        elif():
            return False
    def strightlinescheck(input):
        if input in slines:
            return True
        elif():
            return False
    def curvedlinescheck(input):
        if input in clines:
            return True
        elif():
            return False


vowels = ['A','E','I','O','U']
slines = ['A','E','F','H','I','K','L','M','N','T','V','W','X','Y','Z']
clines = ['B','D','G','J','P','Q','R','U']

userinput1 = int(input ('Please select a mode.\n 1. Vowel Check\n 2. Letters drawn with only straight lines check\n 3. Letters drawn with only curved lines check\n'))

if userinput1 == 1:
    userinput2 = input ('Please enter a Letter: ')
    answer1 = Lettercheck.vowelscheck(userinput2)
    print(answer1)
if userinput1 == 2:
    userinput2 = input ('Please enter a Letter: ')
    answer2 = Lettercheck.strightlinescheck(userinput2)
    print(answer2)
if userinput1 == 3:
    userinput2 = input ('Please enter a Letter: ')
    answer3 = Lettercheck.curvedlinescheck(userinput2)
    print(answer3)