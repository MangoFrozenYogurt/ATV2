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

    for j in words2:
        print(j)

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
    # textwords = []
    # occ = int(0)

    '''for i in arq:
        for j in range(len(i.rsplit())):
            textwords.append(i.rsplit()[j])

        for k in textwords:
            if word == k:
                occ += 1'''

    return str(arq.readlines()).count(word)


def ordstring(string):
    result = int(0)
    for i in range(len(string)):
        result += ord(string[i]) - 96

    return result

# print(occurences('primeira', '../textfiles/teste1.txt'))
