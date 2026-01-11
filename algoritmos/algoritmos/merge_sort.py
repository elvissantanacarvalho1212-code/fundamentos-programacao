def merge_sort(lista):
    operacoes = 0

    if len(lista) <= 1:
        return lista, operacoes

    meio = len(lista) // 2
    esquerda, op_esq = merge_sort(lista[:meio])
    direita, op_dir = merge_sort(lista[meio:])

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        operacoes += 1
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    operacoes += op_esq + op_dir
    return resultado, operacoes
