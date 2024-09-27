x= int(input('primeiro numero:'))
y= int(input('segundo numero:'))

if x %2 ==0 and y %2 ==0:
    print
elif x %2 ==0:
    print(y)
elif y %2 ==0:
    print(x)
else:
    print(x+y)