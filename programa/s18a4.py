def calcular_clicks (t):
    if 1<=t<=1000:
        return(4*t)
    else:
        return('entrada invalida')
    
t= int(input('digite o numero de pessoas que clicaram no link:'))
resultado =calcular_clicks(t)
print(resultado)