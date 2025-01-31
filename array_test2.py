s = ["flower","flow","flight"]

for i in range(len(s)):
    print(s) #imprime o array quantas vezes o tamanho do array for
    print(i) #imprime o índice do array
    print(s[i]) #imprime o elemento do array
    print(len(s[i])) #imprime o tamanho do elemento do array
    
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j]) #imprime o elemento do array
        print(len(s[i][j])) #imprime o tamanho do elemento do array