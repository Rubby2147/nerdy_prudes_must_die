cargo = input ("digite seu cargo:")
dia = input ("digite dia da semana:")
dias_da_semana_aceito ="segunda,terça,quarta,sexta"
dias_da_semana_não_aceitos ="sabado,domingo"
if cargo == 'estagiario' and dias_da_semana_aceito:
    print ("acesso liberado")
elif cargo == 'gerente':
    print ("acesso liberado")
else: 
    cargo == 'estagiario'and dias_da_semana_não_aceitos
    print("acesso negado")
