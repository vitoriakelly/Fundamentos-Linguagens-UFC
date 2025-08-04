from functools import reduce

#  Recursão pura: fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

#  Funções de alta ordem: filter, map, reduce
def analisar_lista(lista):
    pares = list(filter(lambda x: x % 2 == 0, lista))
    dobrados = list(map(lambda x: x * 2, pares))
    soma_total = reduce(lambda x, y: x + y, dobrados, 0)
    return soma_total

#  Execução de exemplo
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6]
    print("Lista:", numeros)

    resultado = analisar_lista(numeros)
    print("Soma dos pares * 2:", resultado)

    print("Fatorial de 5:", fatorial(5))