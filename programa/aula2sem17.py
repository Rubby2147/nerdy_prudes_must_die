distancia = int(input('digite a distancia percorrida em quilometros:'))
combustivel = float(input('digite a quantidade de combustivel gasto em litros'))
consumo = distancia / combustivel
print('=' *50)
print('seu automovel tem consumo medio de {:.3f}km/'.format(consumo))
print('='*50)