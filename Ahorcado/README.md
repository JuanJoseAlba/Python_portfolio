--------------------English / Inglés---------------------------

Hangman is a traditional game where you must guess a word by giving letter by letter and little by little completing the word until you guess it or until the player runs out of lives and the word is revealed.

The program is designed as follows: First, what I do is ask the user through some print in which language he wants to run the program and depending on what he selects is the language in which it will be executed, the language selection is done through an "if".

Second, at the top of the whole I import the libraries that I will use, in this case there are two "random" and "string" and besides that, I bring what I need from the other files that are inside the folder, which are , the words allowed for the hanged man, both in Spanish and English, as the visualization of lives.

Third, I define a function, which will be in charge of choosing a word at random and by means of a "while" I make sure that it does not contain spaces or hyphens and if it does, discard the word and search for another, finally return the word in capital letter.

Fourth, I create another function where all the logic of the game itself will be:

     1. I create the necessary variables for its development, which are words, where I will store the word to be guessed, I also have "letters to guess" which are the letters that I have not yet said, guessed letters, the alphabet, which I take String from the library and in capital letters to be able to compare and finally, I tell him that he has 7 lives.

     2.Now what I do is create a "while" that will be executed while there are still letters to guess or have lives.

     3. Inside the "while" what is found is an "if" in which, depending on the lives, it shows a message on the screen, with the lives it has and the letters it has used.

     4.Then I show the current state of the word, so what I do is that for each letter in the word, what we do is include that letter if it is in "guessed letters" and if it is not, show a " _".

     5.I print the current state of the hangman and also show the current state of the word.

     6.Then I prompt the user for a letter again and convert it to uppercase.

     7. I process the letter of the user, if the letter that the user chooses is within the alphabet and is not within the set of "guessed letters" what I do is add that letter to the set of "guessed letters" by means of an "add".

     8.I find out if the letter is in the word or not, then if it is, I remove the letter from "letters to guess" using a "remove" and if it wasn't, what I do is take a life from the user.

     9.In the event that the letter had already been chosen before, a message is simply displayed on the screen saying that the letter has already been chosen and that you must choose one.

     10.In case of choosing an invalid letter like "Ñ" or something like that, a message will be displayed telling you that the letter is not valid.

     11.At the "while" level I do an "if" where I evaluate if the player still has lives, in case of not having more lives, what I do is show the visual of the hanged doll and I send a message saying that he lost and I show what was the word

     12.In case he guessed the word, a message is displayed saying that he won and shows the word he guessed.

     13. Finally I call the function and that's it.
     

--------------------Español / Spanish--------------------------

Ahorcado es un tradicional juego en donde se debe adivinar una palabra dando letra por letra y poco a poco ir completando la palabra hasta adivinarla o hasta que el jugador se quede sin vidas y la palabra sea revelada.

El programa se diseño de la siguiente manera: Primero lo que hago es preguntarle al usuario por medio de unos print en que idioma desea ejecutar el programa y dependiendo de lo que seleccione es el idioma en que se ejecutará, la seleccion de idioma se hace mediante un "if".

Segundo, en la parte de arriba del todo importo las librerias que usaré, en este caso son dos "random" y "string" y ademas de eso, traigo lo que necesito de los otros archivos que estan dentro de la carpeta, los cuales son, las palabras permitidas para el ahorcado, tanto en español como en ingles, como la visualización de las vidas.

Tercero, defino una función, la cual se encargará de elegir una palabra al azar y mediante un "while" me aseguro de que no contenga espacios o guines y en caso de tenerlo, deseche la palabra y busque otra, por ultimo retorno la palabra en mayúscula.

Cuarto, creo otra funcion en donde estará toda la logica del juego en si:

    1.Creo las variables necesarias para su desarrollo, las cuales son palabra, en donde almacenare la palabra que se debe adivinar, tambien tengo "letras por adivinar" que son las letras que aún no he dicho, letras adivinadas, el alfabeto, que lo saco de la libreria String y en mayuscula para poder comparar y por ultimo, le digo que tiene 7 vidas.

    2.Ahora lo que hago es crear un "while" que se ejecutara mientras aun falten letras por adivinar o tenga vidas.

    3.Dentro del "while" lo que se encuentra es un "if" en el cual dependiendo de las vidas muestra un mensaje en pantalla, con las vidas que tiene y las letras que ha usado.

    4.Luego muestro el estado actual de la palabra, entonces lo que hago es que para cada letra en la palabra, lo que hacemos es que incluya esa letra si esta en "letras adivinadas" y en caso de no ser asi, muestre un "_".

    5.Imprimo el estado actual del ahorcado y tambien muestro el estado actual de la palabra.

    6.Luego vuelvo a pedirle una letra al usuario y la convierto en mayúscula.

    7.Proceso la letra del usuario, si la letra que elige el usuario esta dentro del alfabeto y no esta dentro del conjunto de "letras adivinadas" lo que hago es agregar esa letra al conjunto de "letras adivinadas" mediante un "add".

    8.Averiguo si la letra esta en la palabra o no, entonces en caso de estar, quito la letra de "letras por adivinar" mediante un "remove" y si no estaba lo que hago es quitarle una vida al usuario.

    9.En caso de que la letra ya la hubieran elegido antes, simplemente se muestra un mensaje en pantalla que dice que la letra ya se eligió y que debe elegir una.

    10.En caso de elegir alguna letra no valida como "Ñ" o algo por el estilo, se mostrará un mensaje que le dice que la letra no es valida.

    11.Al nivel del "while" hago un "if" en donde evaluo si aun tiene vidas el jugador, en caso de no tener mas vidas, lo que hago es mostrar la visual del muñeco ahorcado y mando un mensaje diciendo que perdió y muestro cual era la palabra.

    12.En caso de que adivinará la palabra, se muestra un mensaje que dice que ganó y muestra la palabra que adivinó.

    13.Por ultimo hago llamado de la función y listo.
