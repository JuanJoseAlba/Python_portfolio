#Mad libs o historias locas 

print("---------------------------------------------------")
print("Si desea ejecutar el programa en español digite 1 y si lo desea ejecutar en inglés, digite 2.")
print("If you would like to run de programm in spanish mark 1 and if you would like to run the programm in english, mark 2")
print("---------------------------------------------------")
idioma = int(input("Digite una opción / Type an option: "))
print("---------------------------------------------------")

if idioma == 1:

    interjeccion = input("Escriba una interjección: ")
    adverbio = input("Escriba un adverbio: ")
    nombre = input("Escriba un nombre: ")
    adjetivo = input("Escriba un adjetivo femenino: ")

    madlib_esp = f"{interjeccion}! -dijo {adverbio} mientras subia de un salto a su {nombre}, \n un convertible que le encantaba y se marchaba con su {adjetivo} esposa."

    print(madlib_esp)

elif idioma == 2:

    interjection = input("Escriba una interjección: ")
    adverb = input("Escriba un adverbio: ")
    name1 = input("Escriba un nombre: ")
    adjetive = input("Escriba un adjetivo femenino: ")

    madlib_eng = f"{interjection}! -said {adverb} as he jump on his {name1}, \n a convertible that he loved and left with his {adjetive} wife."

    print(madlib_eng)

else:
    print("Opción incorrecta.")
    print("Wrong option.")