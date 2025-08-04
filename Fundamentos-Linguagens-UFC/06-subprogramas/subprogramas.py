def dobrar_elementos(lista):
    for i in range(len(lista)):
        lista[i] *= 2
    print("Dentro da função:", lista)

valores = [1, 2, 3]
print("Antes da função:", valores)
dobrar_elementos(valores)
print("Depois da função:", valores)
