import random
while True:
    dice=int(input('how many diferente rolls are you gonna make:'))
    for i in range(dice):
        dsize=int(input('what is the dice size:'))
        avg=int(input('how many rolls are you making:'))    
        bonus=int(input('what is your bonus to the roll:'))
        solv=[random.randint(1,dsize) for x in range(avg)]
        suma=sum(solv)
        
        print(solv,'+',bonus,"=",(suma+bonus))
    print('='*50)

