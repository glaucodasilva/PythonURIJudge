pal01 = input()
pal02 = input()
pal03 = input()

if pal01 == 'vertebrado':
    if pal02 == 'ave':
        if pal03 == 'carnivoro':
            animal = 'aguia'
        elif pal03 == 'onivoro':
            animal = 'pomba'
    elif pal02 == 'mamifero':
        if pal03 == 'onivoro':
            animal = 'homem'
        elif pal03 == 'herbivoro':
            animal = 'vaca'
elif pal01 == 'invertebrado':
    if pal02 == 'inseto':
        if pal03 == 'hematofago':
            animal = 'pulga'
        elif pal03 == 'herbivoro':
            animal = 'lagarta'
    elif pal02 == 'anelideo':
        if pal03 == 'hematofago':
            animal = 'sanguessuga'
        elif pal03 == 'onivoro':
            animal = 'minhoca'

print(animal)