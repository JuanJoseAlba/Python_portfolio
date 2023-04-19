#Adivina el numero - Guess the number
import random

print("---------------------------------------------------")
print("Si desea ejecutar el programa en español digite 1 y si lo desea ejecutar en inglés, digite 2.")
print("If you would like to run de programm in spanish mark 1 and if you would like to run the programm in english, mark 2")
print("---------------------------------------------------")
idioma = int(input("Digite una opción / Type an option: "))
print("---------------------------------------------------")

if idioma == 1:
 

    def adivina_numero(num):
        print("-------------------------")
        print("Bienvenido")
        print("-------------------------")
        print("Debe adivinar el número que la computadora genere.")

        num_aleatorio = random.randint(0, num)
        prediccion = -1 

        while prediccion != num_aleatorio:
            prediccion = int(input(f"Debes adivinar un numero el cual se encuentra entre 0 y {num}: "))

            if prediccion < num_aleatorio:
                print("El numero es menor, intenta con uno mayor")
            elif prediccion > num_aleatorio:
                print("El numero es mayor, intenta con un numero menor")

        print(f"Felicitaciones, adivinaste el numero!! {num_aleatorio} correctamente.")


    adivina_numero(10)

elif idioma == 2:


    def guess_number(num):
        print("-------------------------")
        print("Welcome")
        print("-------------------------")
        print("Must guess the number that the computer generates.")

        num_random = random.randint(0, num)
        prediction = -1 

        while prediction != num_random:
            prediction = int(input(f"You need to guess the number that is between 0 and {num}: "))

            if prediction < num_random:
                print("the number it's minor, try with one higher")
            elif prediction > num_random:
                print("The number it's higher, try with one lower")

        print(f"Congratulations, you guess the number!! {num_random} correctly.")


    guess_number(10)


else:
    print("Opción incorrecta.")
    print("Wrong option.")


