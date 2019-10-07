import random
import time

movimentacao = 0

#Quicksort variante Lomuto (pivô esquerda)

def quicksort(vetor, inicio, fim):
    #condição de parada
    if inicio < fim:
        pivo = particionar(vetor, inicio, fim)
        quicksort(vetor, inicio, pivo-1) #pivotar a esquerda (ordenar os elementos menores que o pivô)
        quicksort(vetor, pivo+1, fim) #pivotar a direita (ordenar os elemtentos maiores que o pivô)

def particionar(vetor, inicio, fim):
    x = vetor[inicio] #pivô (é o primeiro elemento da esquerda)
    i = inicio #destino final do pivô
    j = inicio + 1 #contador para percorrer o restante do vetor

    #percorrer o vetor
    while j <= fim:
        if vetor[j] > x:
            i += 1 #detectou-se um elemnto menor que o pivô, incrementa o i
            trocar(vetor, i, j)
            global movimentacao
            movimentacao += 1
        j += 1 #passa para o próximo elemento
    trocar(vetor, inicio, i)

    return i

def trocar(vetor, n, m):
    temp = vetor[n]
    vetor[n] = vetor[m]
    vetor[m] = temp

vetor = []
for i in range(2500):
    vetor.append(random.randint(0,3999))

antes = time.time()
quicksort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois-antes)*1000

print(vetor)
print("O tempo total foi: %0.2f ms" % total)
print("Numero de movimentações:", movimentacao)