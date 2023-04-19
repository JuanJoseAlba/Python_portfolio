#Hangman game - juego del ahorcado
import random
import string
from words import palabras
from words import words
from hangman_visual import hangman_visual


print("---------------------------------------------------")
print("Si desea ejecutar el programa en español digite 1 y si lo desea ejecutar en inglés, digite 2.")
print("If you would like to run de programm in spanish mark 1 and if you would like to run the programm in english, mark 2")
print("---------------------------------------------------")
idioma = int(input("Digite una opción / Type an option: "))
print("---------------------------------------------------")


if idioma == 1:


    def obtener_palabra(palabras):
        palabra =  random.choice(palabras)

        while '-' in palabra or ' ' in palabra:
            palabra = random.choice(palabras)

        return palabra.upper() 


    def ahorcado():

        print("-------------------")
        print("Bienvenido")
        print("-------------------")

        palabra = obtener_palabra(palabras)

        letras_por_adivinar = set(palabra)
        letras_adivinadas = set()
        alfabeto = set(string.ascii_uppercase)

        vidas = 7

        while len(letras_por_adivinar) > 0 and vidas > 0:

            if vidas == 1:
                print(f"Tiene {vidas} vida y ha usado las siguientes letras: {' '.join(letras_adivinadas)}")
            else:
                print(f"Tienes {vidas} vidas y ha usado las siguientes letras: {' '.join(letras_adivinadas)}")

            palabra_lista = [letra if letra in letras_adivinadas 
                            else '_' for letra in palabra]
            
            print(hangman_visual[vidas])
            print(f"Palabra: {' '.join(palabra_lista)}")

            letra_usuario = input("Elegir una letra: ").upper()

            if letra_usuario in alfabeto - letras_adivinadas:
                letras_adivinadas.add(letra_usuario)

                if letra_usuario in letras_por_adivinar:
                    letras_por_adivinar.remove(letra_usuario)
                    print('')
                else:
                    vidas = vidas - 1
                    print(f"Tu letra, {letra_usuario} no se encuentra en la palabra")
            elif letra_usuario in letras_adivinadas:
                print("Ya elegiste esta letra, selecciona otra")
            else:
                print("Esta letra no es valida")
        
        if vidas == 0:
            print(hangman_visual[vidas])
            print(f"Perdiste, la palabra era {palabra}")
        else:
            print(f"Ganaste, adivinaste la palabra: {palabra}")


    ahorcado()

elif idioma == 2:
    

    def get_word(words):
        word =  random.choice(words)

        while '-' in word or ' ' in word:
            word = random.choice(words)

        return word.upper() 


    def hangman():

        print("-------------------")
        print("Welcome")
        print("-------------------")

        word = get_word(words)

        letters_to_guess = set(word)
        guessed_letters = set()
        alphabet = set(string.ascii_uppercase)

        lives = 7

        while len(letters_to_guess) > 0 and lives > 0:

            if lives == 1:
                print(f"You have {lives} life and you used this letters: {' '.join(guessed_letters)}")
            else:
                print(f"You have {lives} lives and you used this letters: {' '.join(guessed_letters)}")

            word_list = [letter if letter in guessed_letters 
                            else '_' for letter in word]
            
            print(hangman_visual[lives])
            print(f"Word: {' '.join(word_list)}")

            user_letter = input("Choice a letter: ").upper()

            if user_letter in alphabet - guessed_letters:
                guessed_letters.add(user_letter)

                if user_letter in letters_to_guess:
                    letters_to_guess.remove(user_letter)
                    print('')
                else:
                    lives = lives - 1
                    print(f"Your letter, {user_letter} is not in the word")
            elif user_letter in guessed_letters:
                print("you already chose this letter, try with another one.")
            else:
                print("Invalid letter")
        
        if lives == 0:
            print(hangman_visual[lives])
            print(f"You lost, the word is {word}")
        else:
            print(f"You win, you guessed the word: {word}")


    hangman()


else:
    print("Opción incorrecta.")
    print("Wrong option.")

