from cpf import validaCPF, validar_cnpj, validar_cpf_cnpj


# --- CPF (garantir que a validação anterior continua funcionando) ---
def test_cpf_valido():
    assert validaCPF("529.982.247-25") is True


def test_cpf_invalido():
    assert validaCPF("111.111.111-11") is False
    assert validaCPF("123.456.789-09") is False


# --- CNPJ ---
def test_cnpj_valido_com_mascara():
    assert validar_cnpj("11.222.333/0001-81") is True
    assert validar_cnpj("04.252.011/0001-10") is True


def test_cnpj_valido_sem_mascara():
    assert validar_cnpj("11222333000181") is True


def test_cnpj_invalido():
    assert validar_cnpj("11.222.333/0001-00") is False


def test_cnpj_tamanho_incorreto():
    assert validar_cnpj("11.222.333/0001") is False
    assert validar_cnpj("112223330001") is False


def test_cnpj_todos_digitos_iguais():
    assert validar_cnpj("11111111111111") is False
    assert validar_cnpj("00.000.000/0000-00") is False


# --- CPF ou CNPJ ---
def test_validar_cpf_cnpj_misto():
    assert validar_cpf_cnpj("529.982.247-25") is True    # CPF válido
    assert validar_cpf_cnpj("111.111.111-11") is False   # CPF inválido
    assert validar_cpf_cnpj("11.222.333/0001-81") is True   # CNPJ válido
    assert validar_cpf_cnpj("11.222.333/0001-00") is False  # CNPJ inválido


def test_validar_cpf_cnpj_tamanho_invalido():
    assert validar_cpf_cnpj("123") is False
    assert validar_cpf_cnpj("") is False
