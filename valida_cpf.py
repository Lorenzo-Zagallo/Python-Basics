def valida_cpf(cpf):
    #remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    #validar quantidade de dígitos
    if len(cpf) != 11:
        return False
    
    #validar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    #calcular primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i) # multiplica o caractere na posição i com 10 - i (ex: 9 * 10 - 0)
    primeiro_digito = 11 - (soma % 11)
    primeiro_digito = 0 if primeiro_digito >= 10 else primeiro_digito

    #validar primeiro dígito
    if int(cpf[9]) != primeiro_digito:
        return False

    #calcular segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = 11 - (soma % 11)
    segundo_digito = 0 if segundo_digito >= 10 else segundo_digito

    #validar segundo dígito
    if int(cpf[10]) != segundo_digito:
        return False
    
    return True

#testando a função
cpf_testes = [
    "111.111.111-11",  # inválido (todos os dígitos iguais)
    "123.456.789-09",  # pode ser válido
    "123.456.789-00"   # inválido (para teste)
]

for cpf in cpf_testes:
    if valida_cpf(cpf):
        print(f"{cpf} é um CPF válido.")
    else:
        print(f"{cpf} é um CPF inválido.")

input("Pressione <enter> para encerrar...")
