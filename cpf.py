

# Função para validar CPF
def validaCPF(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(set(cpf)) == 1:
        return False
    else:
        soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto1 = (soma1 * 10) % 11
        if resto1 == 10:
            resto1 = 0

        soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto2 = (soma2 * 10) % 11
        if resto2 == 10:
            resto2 = 0

        if resto1 == int(cpf[9]) and resto2 == int(cpf[10]):
            return True
        else:
            return False