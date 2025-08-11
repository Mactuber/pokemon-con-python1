from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95

TAMANIO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    print("\n==========================")
    print("Turno de Pikachu")  # Turno Pikachu
    ataque_pikachu = randint(1, 2)

    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    # Ajustar vida mínima
    if vida_squirtle < 0:
        vida_squirtle = 0

    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    # Si Squirtle muere tras el ataque de Pikachu, se termina el combate antes de su turno
    if vida_squirtle == 0:
        break

    input("Enter para continuar...\n\n")
    os.system("cls")

    print("\nTurno de Squirtle")  # Turno Squirtle
    ataque_squirtle = ""
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ").upper()

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada")

    if vida_pikachu < 0:
        vida_pikachu = 0

    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("cls")

# Resultado final
print("\n==========================")
if vida_pikachu <= 0 and vida_squirtle <= 0:
    print("¡Empate!")
elif vida_pikachu > vida_squirtle:
    print("¡Pikachu gana!")
else:
    print("¡Squirtle gana!")
