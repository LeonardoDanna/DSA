def staircase(n):
    for i in range(n):
        print(" "*(n-i-1) + "#"*(i+1))
        
        #se n = 5 então vai printar 4 espaços e 1 #, depois 3 espaços e 2 #, depois 2 espaços e 3 #, depois 1 espaço e 4 #, depois 0 espaços e 5 #
        
staircase(15)