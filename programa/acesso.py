cargo = input ("digite seu cargo:")
dia = input ("digite dia da semana:")
if cargo == ('estagiario') and dia == ('segunda','terça','quarta','quinta','sexta'):
    print ("acesso permitido")
elif cargo == "estagiario" and dia == ('sabado', 'domingo'):
    print ("acesso negado")
else: 
    print ("acesso negado")




  