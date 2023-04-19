#rock, paper, scissors o piedra, papel o tijeras
import random

print("---------------------------------------------------")
print("Si desea ejecutar el programa en español digite 1 y si lo desea ejecutar en inglés, digite 2.")
print("If you would like to run de programm in spanish mark 1 and if you would like to run the programm in english, mark 2")
print("---------------------------------------------------")
idioma = int(input("Digite una opción / Type an option: "))
print("---------------------------------------------------")

if idioma == 1:
    def juego():
        jugador = input("Seleccionar la opción que desea, 'piedra' para piedra, 'papel' para papel y 'tijera' para tijeras: ").lower()
        cpu = random.choice(["piedra", "tijera", "papel"])
        print("La computadora eligió: " + cpu)
        
        if jugador == cpu:
            print("Empate!")
        elif jugador_gana (jugador, cpu):
            print("Ganaste!")    
        else:
            print("Perdiste!")

    def jugador_gana(retador, oponente):

        if ((retador == "piedra" and oponente == "tijera")
            or (retador == "tijera" and oponente == "papel")
            or (retador == "papel" and oponente == "piedra")
        ):
            return True
        else:
            return False
        
    print(juego())

elif idioma == 2:
    def game():
        player = input("select the option that you prefer, 'rock' to rock, 'paper' to paper and 'scissors' to scissors: ").lower()
        cpu = random.choice(["rock", "paper", "scissors"])
        print("The pc select: " + cpu)
        
        if player == cpu:
            print("Draw!")
        elif player_win (player, cpu):
            print("You Win!")    
        else:
            print("You lost!")

    def player_win(defiant, opponet):

        if ((defiant == "rock" and opponet == "scissors")
            or (defiant == "scissors" and opponet == "paper")
            or (defiant == "paper" and opponet == "rock")
        ):
            return True
        else:
            return False
        
    print(game())

else:
    print("Opción incorrecta.")
    print("Wrong option.")








