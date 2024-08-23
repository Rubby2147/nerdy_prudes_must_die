def calcular_distancia(t,v):
    if 1<= t <=100 and 0 <= v <=120:
        return t*v
    elif t== 0 or v == 0:
        return 0
    else:
        return -1
    
t1, v1 = map(int, input('digite o tempo e a velocuidade para o intervalo:').split())
t2, v2 = map(int, input('digite o tempo e a velocuidade para o intervalo:').split())
t3, v3 = map(int, input('digite o tempo e a velocuidade para o intervalo:').split())

distancia1 = calcular_distancia(t1,v1)
distancia2 = calcular_distancia(t2,v2)
distancia3 = calcular_distancia(t3,v3)

if distancia1 == -1 or distancia2 == -1 or distancia3 == -1:
    print ('entrada invalida')
else: 
    distanciatotal = distancia1 + distancia2 + distancia3
    print('distancia percorrida é', distanciatotal)
