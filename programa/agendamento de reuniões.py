pessoas= int(input('quantas pessoas vão participar da reunião:'))
tipo_de_reunião= (input('reunião sera executiva ou normal:'))
if pessoas <=5 and tipo_de_reunião=='normal':
    print ('a reuiniaõ sera em sala pequena')
elif pessoas >=6 and pessoas <15 and tipo_de_reunião=='normal':
    print('a reuiniaõ sera em sala media')
else: pessoas >=15 and tipo_de_reunião=='normal' or tipo_de_reunião=='executivo'
print('a reuiniaõ sera em sala executiva')