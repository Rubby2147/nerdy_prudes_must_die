def recomendar_sala (pessoas, tipo_de_reunião):
    if pessoas <=5:
        return ('a reuiniaõ sera em sala pequena')
    elif pessoas <=15:
        return('a reuiniaõ sera em sala media')
    elif pessoas>15:
        return ('a reunião sera na sala executiva')
    else: tipo_de_reunião == 'executivo'
    return('a reunião sera na sala executiva')
pessoas= int(input('quantas pessoas vão participar da reunião:'))
tipo_de_reunião= (input('reunião sera executiva ou normal:'))
if pessoas <=0:
    print ('numero de participantes invalido')
elif tipo_de_reunião not in ['normal','executiva']:
    print('tipo de reunião invalida')
else:
    recomendar_sala = recomendar_sala(pessoas, tipo_de_reunião)
    print (f'a sala recomendada é:{recomendar_sala}')

