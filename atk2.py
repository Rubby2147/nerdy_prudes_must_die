def calc_damage (dado,ataques,bonus,dano,crit,ac):
    hc = (1-pow(((ac-bonus)/20),dado))
    ataque=(ataques*(hc*(dano))+(dado/20)*crit)
    return ataque

ac=int(input('qual ac quer acertar:'))
atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))

resultados= []
for x in (range(atk)):
    ataques= int(input('quantos ataques iguais vai fazer:'))
    dado = int(input('quantos dados vai rolar:')) 
    bonus= int(input('qual seu bonus para acertar:'))
    dano=int(input('dano por cada ataque:'))
    crit =int(input('dano em um critico:'))
    print('='*50)
fatores  = [dado,ataques,bonus,dano,crit]

resultado = float[calc_damage(*fatores,ac)]
resultados.append(resultado)

total_de_dano = sum(resultados)

