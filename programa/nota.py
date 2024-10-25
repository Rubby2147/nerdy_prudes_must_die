validas= 0
notas=[]

while validas<4:
    n=float(input('digite notas:'))
    if n >0 and n<=10:
        notas.append(n)
        validas+=1
    else:
        print('invalida')

print('sua notas foram:',sorted(notas))
print('sua media foi:',sum(notas)/len(notas))
print('sua maior nota foi:',max(notas))
