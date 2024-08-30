list = []
for i in range(10):
    n = int(input('digite um numero'))
    list.append(n)
soma = sum(list)
maior = max(list)
menor = min(list)

print (f'a soma ={soma}')
print (f'a maior ={maior}')
print (f'a menor ={menor}')