import random
import time

from algoritmos.bubble_sort import bubble_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort


def gerar_lista(tamanho):
    return [random.randint(0, 10000) for _ in range(tamanho)]


def testar_algoritmo(nome, funcao, lista):
    copia = lista.copy()
    inicio = time.time()
    _, operacoes = funcao(copia)
    fim = time.time()

    print(f"{nome}")
    print(f"Tempo: {fim - inicio:.6f}s")
    print(f"Operações: {operacoes}")
    print("-" * 30)
