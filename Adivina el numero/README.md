--------------------English / Inglés---------------------------

Guess the number is a simple game where the user must guess the number that the computer randomly selects.

The program was developed in the following way, the user is asked by means of some print in which language he wishes to execute the program and depending on what he selects is the language in which it will be executed, the language selection is made by means of an "if ".

Then, what I do is that I create a function called "guess_number" which receives an argument, which is the one that defines the limit of the range in which the number to be guessed will be, then through "random.randint" which It allows me to select a random integer number from a given range, and I create a "prediction" variable with a value outside the range so that it can't match the number to guess from the beginning.
Then through a "while" which is programmed to stop when the prediction and the random number are the same, that is, when the user guesses the number, there inside the "while" I show a message where the user is told in which range you must guess the number and by means of an "if" it is told if it is greater than the number or less and to finish, by means of a "print" it throws a message saying that it guessed the number and the function is called with the value of the argument.


--------------------Español / Spanish--------------------------

Adivina el numero es un simple juego en donde el usuario debe adivinar el numero que la computadora selecciona al azar.

El programa se desarrollo de la siguiente manera, se le pregunta al usuario por medio de unos print en que idioma desea ejecutar el programa y dependiendo de lo que seleccione es el idioma en que se ejecutará, la seleccion de idioma se hace mediante un "if".

Luego, lo que hago es que creo una función que se llama "adivina_numero" la cual recibe un argumento, el cual es el que define el limite del rango en el que estará el numero a adivinar, luego mediante "random.randint" el cual me permite seleccionar un numero aletario entero entre un rango dado, y creo una variable "prediccion" con un valor fuera del rango para que no pueda coincidir desde el principio con el numero a adivinar.
Luego mediante un "while" el cual se programa para que se detenga cuando la predicción y el numero aleatorio sean iguales, es decir, cuando el usuario adivine el numero, allí dentro del "while" muestro un mensaje en donde se le dice al usuario en que rango debe adivinar el numero y por medio de un "if" se le va diciendo si es mayor al numero o menor y ya para finalizar, mediante un "print" arroja un mensaje diciendole que adivinó el numero y se llama a la funcion con el valor del argumento.
