def recomendar_sala (pessoas, tipo_de_reunião):
    if pessoas <=5 and tipo_de_reunião=='normal':
        return ('a reuiniaõ sera em sala pequena')
    elif pessoas >=6 and pessoas <15 and tipo_de_reunião=='normal':
        return('a reuiniaõ sera em sala media')
    else: pessoas >=15 and tipo_de_reunião=='normal' or tipo_de_reunião=='executivo'
    return('a reunião sera na sala executiva')
