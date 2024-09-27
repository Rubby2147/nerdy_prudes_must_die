def maior3(a,b,c):
    if  a>=b and a>=c:
        return 'a é maior'
    elif b>=a and b >=c:
        return 'b é maior'
    else: c>a and c>b
    return 'c é maior'

n1= (int(input('numero a:')))
n2= (int(input('numero b:')))
n3= (int(input('numero c:')))

resultado = maior3(n1,n2,n3)
print (resultado)