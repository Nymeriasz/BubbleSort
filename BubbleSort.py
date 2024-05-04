def bubbleSort(vetor):
    n = len(vetor)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

vetor = [1, 3, 5, 4, 2, 6, 8, 7, 10, 9]
bubbleSort(vetor)
print(vetor)