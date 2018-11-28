n = int(input())
for i in range(n):
    sheldon, raj = input().split()
    if sheldon == raj:
        print('Caso #%i: De novo!' %(i+1))
    elif sheldon == 'tesoura' and raj == 'papel':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'papel' and raj == 'pedra':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'pedra' and raj == 'lagarto':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'lagarto' and raj == 'Spock':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'Spock' and raj == 'tesoura':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'tesoura' and raj == 'lagarto':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'lagarto' and raj == 'papel':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'papel' and raj == 'Spock':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'Spock' and raj == 'pedra':
        print('Caso #%i: Bazinga!' %(i+1))
    elif sheldon == 'pedra' and raj == 'tesoura':
        print('Caso #%i: Bazinga!' %(i+1))
    else:
        print('Caso #%i: Raj trapaceou!' %(i+1))