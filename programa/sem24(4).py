num_itens = int(input('quentidade de items:'))

inventario=[]

for i in range(num_itens):
    nome=input(f'nome do iten{i+1}:')
    categoria=input(f'categoria do iten{i+1}:')
    quantidade=input(f'quantidade do iten{i+1}:')

    inventario.append((nome,categoria,quantidade))
print('\ninventario completo')
for item in inventario:
    print(f'nome:{item[0]}')
    print(f'categoria:{item[1]}')
    print(f'quantidade:{item[2]}')