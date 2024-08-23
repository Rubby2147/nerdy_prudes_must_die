pares = 0
inpares = 0
for cont in range(4):
    num = int(input('digite um numero'))
    if num %2 ==0:
        pares +=1

    elif num %2 != 0:
        inpares +=1

print (f'quantidade de num, pares é:{pares}')
print (f'quantidade de num, inpares é:{inpares}')