
apagar = 0
while True:
        codigo = int(input('qual o codigo do produto:'))
        preço = 0
        if codigo == 0:
            break
        elif codigo ==1:
            preço =0,50
        elif codigo ==2:
            preço =1,00
        elif codigo ==3:
            preço =4,00
        elif codigo ==5:
            preço =7,00
        elif codigo ==9:
            preço =8,00
        else:
             print ('codigo invalido')
if preço!= 0:
    quantidade = int(input('quantidade:'))
    apagar = apagar +(preço*quantidade)