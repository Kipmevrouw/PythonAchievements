import random

original = "hallo"

def functie(original):
    randomised = ''.join(random.sample(original, len(original)))
    return str(randomised)

print(functie("Becky is een idioot"))
print(functie("Becky is een aardig persoon"))
print(functie("Becky is geweldig"))









