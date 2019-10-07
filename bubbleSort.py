import random
import time

movimentacao = 0

def bubbleSort(vetor):

    final = len(vetor)

    while final > 0:
        i = 0
        #Percorrendo o vetor de 0 até final.
        while i < final - 1:
            #Testando a condição para checar se o meu par está ordenado
            if vetor[i] < vetor[i + 1]:
                #Realizando a troca da posição atual pela próxima.
                temp = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = temp
                #Incrementando a variavel responsavel por registrar o número de trocas.
                global movimentacao
                movimentacao += 1
            i += 1
            #Decrementando a variavel responsavel por terminar a verificação do vetor
        final -= 1

vetor = []
for i in range(2500):
    vetor.append(random.randint(0,3999))

antes = time.time()

bubbleSort(vetor)

depois = time.time()

total = (depois - antes)*1000

print(vetor)
print("Tempo de execução %0.2f ms" %total)
print("Numero de movimentações:", movimentacao)
