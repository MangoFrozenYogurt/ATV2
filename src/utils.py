def listwords(file):
    arq = open(file)
    words = []
    for i in arq:
        for j in range(len(i.rsplit())):
            words.append(i.rsplit()[j])

    words2 = []

    for i in words:
        if i not in words2:
            words2.append(i)

    '''for j in words2:
        print(j)
    '''
    arq.close()
    return words2


def numwords(file):
    arq = open(file)
    words = []
    for i in arq:
        for j in range(len(i.rsplit())):
            words.append(i.rsplit()[j])

    return len(words)


def occurences(word, file):
    arq = open(file)
    qt = str(arq.readlines()).count(word)
    arq.close()
    return qt


def ordstring(string):
    result = int(0)
    for i in range(len(string)):
        result += ord(string[i]) - 96

    return result


def merge_sort(colecao):

    if len(colecao) > 1:
        meio = int(len(colecao) / 2)
        esqpart = colecao[:meio]  # cortando colecao no meio e atribuindo a primeira metada a esqpart
        dirpart = colecao[meio:]  # segunda metade a dirpart

        # esqpart e dirpart são subarrays ou sublists
        # chamadas recursivas
        merge_sort(esqpart)
        merge_sort(dirpart)

        i = 0 # indice inicial esqpart
        j = 0 # indice inicial dirpart
        k = 0 # indice inicial da colecao

        while i < len(esqpart) and j < len(dirpart):

            # dividindo colecao em dois subarrays

            if int(esqpart[i].key) < int(dirpart[j].key):
                colecao[k] = esqpart[i]
                i += 1
            else:
                colecao[k] = dirpart[j]
                j += 1
            k += 1

        while i < len(esqpart):

            # mesclando subarrays na colecao

            colecao[k] = esqpart[i]
            i += 1
            k += 1

        while j < len(dirpart):
            colecao[k] = dirpart[j]
            j += 1
            k += 1

    return colecao


def ordenar(colecao):
    return merge_sort(colecao)

# print(occurences('primeira', '../textfiles/teste1.txt'))
