""" Linting Test """

def count(sequence, item):
    """ Count function """
    numbervar = 0
    for number in sequence:
        if number == item:
            numbervar += 1
    return numbervar
