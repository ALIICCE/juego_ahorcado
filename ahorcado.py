import random

# Lista de palablas que apareceran en el juego
palabras = ["univeridad", "barco", "computadora", "raton", "teclado", "habitacion"]

# Lista que pinta el canva segun los intentos
ahorcado = [
    """
       +---+
           |
           |
           |
          ===""",
    """
       +---+
       O   |
           |
           |
          ===""",
    """
       +---+
       O   |
       |   |
           |
          ===""",
    """
       +---+
       O   |
      /|   |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
]


def intentos_fallidos(letras_adivinadas, palabra):
    return sum(1 for letra in letras_adivinadas if letra not in palabra)

def jugar_ahorcado():
    palabra = random.choice(palabras)
    palabra_oculta = ["_" for _ in palabra]
    letras_adivinadas = []
    intentos = 0
    max_intentos = len(ahorcado) - 1

    while intentos < max_intentos and "_" in palabra_oculta:
        print(ahorcado[intentos])
        print("Fallos:", intentos_fallidos(letras_adivinadas, palabra))
        print("\nLetras ya dichas:", " ".join(letras_adivinadas))
        print("\nPalabra:", "".join(palabra_oculta))

        letra = input("\nAdivina una letra: ").lower() #convierte mayus a minusculas

        if not letra.isalpha() or len(letra) != 1: #valida que sea solo 1 letra
            print("Por favor, introduce solo una letra.\n")
            continue

        if letra in letras_adivinadas: #valida letras repetidas
            print("Ya has dicho esa letra.\n")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    palabra_oculta[i] = letra
        else:
            intentos += 1

    print(ahorcado[intentos])
    if "_" not in palabra_oculta:
        print("\n¡Felicidades! \nAdivinaste la palabra:", palabra)
    else:
        print("\nPerdiste... \nLa palabra era:", palabra)

    jugar_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevo == "s":
        jugar_ahorcado()

# Ejecutar el juego
jugar_ahorcado()
