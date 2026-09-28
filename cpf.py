# Lista de CPFs bloqueados (fakes conhecidos / de teste)
CPFS_BLOQUEADOS = {
    "12345678909",
    "11144477735",   # exemplo clássico usado em testes
    "98765432100",
}

# Sequências óbvias (crescentes e decrescentes)
SEQUENCIAS = {
    "01234567890", "12345678901", "23456789012", "34567890123",
    "45678901234", "56789012345", "67890123456", "78901234567",
    "89012345678", "90123456789",
    "98765432109", "87654321098", "76543210987", "65432109876",
    "54321098765", "43210987654", "32109876543", "21098765432",
    "10987654321", "09876543210",
}


def validaCPF(cpf):
    # 1. Limpa: mantém só dígitos
    cpf = ''.join(filter(str.isdigit, str(cpf)))

    # 2. Checa tamanho ANTES de qualquer acesso a índice
    if len(cpf) != 11:
        return False

    # 3. Rejeita dígitos todos iguais (111..., 222..., etc.)
    if len(set(cpf)) == 1:
        return False

    # 4. Rejeita sequências óbvias
    if cpf in SEQUENCIAS:
        return False

    # 5. Rejeita blacklist de CPFs fake
    if cpf in CPFS_BLOQUEADOS:
        return False

    # 6. Validação matemática dos dígitos verificadores
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = (soma1 * 10) % 11
    if resto1 == 10:
        resto1 = 0

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = (soma2 * 10) % 11
    if resto2 == 10:
        resto2 = 0

    return resto1 == int(cpf[9]) and resto2 == int(cpf[10])


def validar_cnpj(documento):
    """Valida um CNPJ (com ou sem máscara), retornando True/False."""
    # 1. Limpa: mantém só dígitos
    cnpj = ''.join(filter(str.isdigit, str(documento)))

    # 2. Checa tamanho ANTES de qualquer acesso a índice
    if len(cnpj) != 14:
        return False

    # 3. Rejeita dígitos todos iguais (000..., 111..., etc.)
    if len(set(cnpj)) == 1:
        return False

    # 4. Validação matemática dos dígitos verificadores
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    resto1 = soma1 % 11
    dv1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    resto2 = soma2 % 11
    dv2 = 0 if resto2 < 2 else 11 - resto2

    return dv1 == int(cnpj[12]) and dv2 == int(cnpj[13])


def validar_cpf_cnpj(documento):
    """Valida um documento que pode ser CPF (11 dígitos) ou CNPJ (14 dígitos).

    Aceita o valor com ou sem máscara (pontuação) e retorna True/False.
    """
    # Limpa tudo que não for número
    documento = ''.join(filter(str.isdigit, str(documento)))

    if len(documento) == 11:
        return validaCPF(documento)      # Já retorna True/False
    elif len(documento) == 14:
        return validar_cnpj(documento)   # Já retorna True/False

    return False  # Qualquer outra coisa é inválido


# --- Testes ---
if __name__ == "__main__":
    testes_cpf = [
        "123.456.789-09",   # fake conhecido -> False
        "111.111.111-11",   # todos iguais -> False
        "123.456.789",      # tamanho errado -> False
        "012.345.678-90",   # sequência óbvia -> False
        "529.982.247-25",   # válido de verdade -> True
    ]
    for t in testes_cpf:
        print(f"CPF  {t} -> {validaCPF(t)}")

    testes_cnpj = [
        "11.222.333/0001-81",   # válido de verdade -> True
        "11222333000181",       # válido sem máscara -> True
        "04.252.011/0001-10",   # válido de verdade -> True
        "11.222.333/0001-00",   # dígito verificador errado -> False
        "11111111111111",       # todos iguais -> False
        "11.222.333/0001",      # tamanho errado -> False
    ]
    for t in testes_cnpj:
        print(f"CNPJ {t} -> {validar_cnpj(t)}")

    print("--- validar_cpf_cnpj ---")
    mistos = [
        "529.982.247-25",       # CPF válido -> True
        "111.111.111-11",       # CPF inválido -> False
        "11.222.333/0001-81",   # CNPJ válido -> True
        "11.222.333/0001-00",   # CNPJ inválido -> False
        "123",                  # tamanho inválido -> False
    ]
    for t in mistos:
        print(f"{t} -> {validar_cpf_cnpj(t)}")
