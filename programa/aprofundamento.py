cont = True
while cont:
        n = int(input('digite um numero:'))
        for i in range(1,11):
                print (n,'x',i,'=', n*i)    
        resp = input ('deseja continuar? s/n:')
        if resp == 'n':
                cont = False