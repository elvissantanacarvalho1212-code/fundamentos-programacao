from analise.comparador import gerar_lista, testar_algoritmo
from algoritmos.bubble_sort import bubble_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort

TAMANHO = 1000

lista = gerar_lista(TAMANHO)

testar_algoritmo("Bubble Sort", bubble_sort, lista)
testar_algoritmo("Insertion Sort", insertion_sort, lista)
testar_algoritmo("Merge Sort", merge_sort, lista)
