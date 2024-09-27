bugs={
'bug1':['alta',7],
'bug2':['media',4],
'bug3':['baixo',2],
'bug4':['alta',7],
'bug5':['media',8]

}

bugs_prioritarios= {}

for bug, info in bugs.items():
    if info[1]>5:
        bugs_prioritarios[bug] = info

print('relatorio de bugs')
for bug, info in bugs_prioritarios.items():
    print(f'{bug},gravidade:{info[0]}, reportados:{info[1]}')

