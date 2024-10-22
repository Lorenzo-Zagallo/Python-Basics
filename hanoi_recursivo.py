def move_disco(numero, origem, destino, auxiliar):
    if numero == 1:
        print(f"Mover o disco 1 de {origem} para {destino}")
        return
    move_disco(numero - 1, origem, auxiliar, destino)
    print(f"Mover o disco {numero} de {origem} para {destino}")
    move_disco(numero - 1, auxiliar, destino, origem)

def exibir_torres(torres):
    for i, torre in enumerate(torres):
        print(f"Torre {i + 1}: {torre}")
    print()

def torres_de_hanoi(numero):
    torres = [list(range(numero, 0, -1)), [], []]
    print("Estado inicial:")
    exibir_torres(torres)

    move_disco(numero, 'Torre 1', 'Torre 3', 'Torre 2')

    exibir_torres(torres)

if __name__ == "__main__":
    quantidade_de_discos = 3
    torres_de_hanoi(quantidade_de_discos)

input(' ') # <Enter>