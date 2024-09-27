validas = 0
soma = 0
while validas<2:
    notas = int(input('digite as notas'))
    if notas >=0 and notas<10:
        validas +=1
        soma +=notas
    else:
        print ('notas invalidas')

media =soma/2
print (f'media={media}')