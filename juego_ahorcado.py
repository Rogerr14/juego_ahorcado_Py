
import random


def get_secret_word() -> str :
    words = ["python", "java", "angular", "react", "flask"]
    return random.choice(words)

def show_progress(secret_word, letter_match):
    adivinado = ''
    for letter in secret_word:
        if letter in letter_match:
            adivinado += letter
        else:
            adivinado +="_"
    return adivinado


def game():
    secret_word = get_secret_word()
    letter_match =[]
    intents = 7
    game_end = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tienes {intents} intentos para adivinar la palabra")
    print(show_progress(secret_word, letter_match))

    while not game_end and intents > 0:
        adivinanza = input("Introduce una letra: ").lower()
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("introduzca solo una letra")
        elif adivinanza in letter_match:
            print("ya ingresaste esa letra, prueba otra")
        else:
            letter_match.append(adivinanza)

            if(adivinanza in secret_word):
                print(f"Muy bien has acetado, la letra {adivinanza} está en la palabra secreta")
            else:
                intents -=1
                print(f"Error: no existe la letra {adivinanza} no esta en la palabra secreta")
                print(f"Te quedan {intents} intentos")
        
        actual_progress = show_progress(secret_word, letter_match)
        print(actual_progress)
        if "_" not in actual_progress:
            game_end = True
            print(f"Felicitaciones! Ganaste!, la palabra es {secret_word}")

    if intents == 0:
        print(f"Perdiste! la palabra secreta era {secret_word}")

game()
    

