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


# --- Testes ---
if __name__ == "__main__":
    testes = [
        "123.456.789-09",   # fake conhecido -> False
        "111.111.111-11",   # todos iguais -> False
        "123.456.789",      # tamanho errado -> False
        "012.345.678-90",   # sequência óbvia -> False
        "529.982.247-25",   # válido de verdade -> True
    ]
    for t in testes:
        print(f"{t} -> {validaCPF(t)}")
