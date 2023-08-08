var = str(input ("Input word: "))
result = 0

for letters in var:
    if letters == 'a':
        result = result + 1
    if letters == 'e':
        result = result + 1
    if letters == 'i':
        result = result + 1
    if letters == 'o':
        result = result + 1
    if letters == 'u':
        result = result + 1

print(var, 'has', result, 'vowels')