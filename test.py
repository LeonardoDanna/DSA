arr = [1, 3, 2, 5, 4]

def procuraAcha(arr):
    for i in arr:
        print(i)
        
def procuraAcha2(arr):
    for i in range(len(arr)):
        print(i)
        
def procuraAcha3(arr):
    for i in range(len(arr)):
        print(arr[i])
        
def procuraAcha4(arr):
    for i in range(1, len(arr) + 1):
        print(i) 
        
procuraAcha(arr) # printa todos os elementos do array
procuraAcha2(arr) #printa os indices dos elementos do array
procuraAcha3(arr) #printa os elementos do array
procuraAcha4(arr) #printa os indices dos elementos do array