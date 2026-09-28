# CPF

Validador de CPF em Python.

## Descrição

O arquivo [`cpf.py`](./cpf.py) contém a função `validaCPF(cpf)`, que verifica se um
CPF é válido. A validação é defensiva e cobre, além do cálculo dos dígitos
verificadores, algumas regras comuns de rejeição:

1. **Limpeza**: remove qualquer caractere que não seja dígito (aceita entradas
   como `529.982.247-25` ou `52998224725`).
2. **Tamanho**: rejeita entradas que não tenham exatamente 11 dígitos.
3. **Dígitos repetidos**: rejeita CPFs com todos os dígitos iguais
   (ex.: `111.111.111-11`).
4. **Sequências óbvias**: rejeita sequências crescentes/decrescentes
   (ex.: `012.345.678-90`).
5. **Blacklist**: rejeita uma lista de CPFs fake conhecidos/de teste.
6. **Dígitos verificadores**: valida matematicamente os dois últimos dígitos.

A função retorna `True` para um CPF válido e `False` caso contrário.

## Uso

### Como função

```python
from cpf import validaCPF

validaCPF("529.982.247-25")  # True
validaCPF("111.111.111-11")  # False
```

### Executando os testes de exemplo

O script traz alguns casos de teste embutidos, executados ao rodá-lo diretamente:

```bash
python cpf.py
```

Saída esperada:

```
123.456.789-09 -> False
111.111.111-11 -> False
123.456.789 -> False
012.345.678-90 -> False
529.982.247-25 -> True
```

## Requisitos

- Python 3 (sem dependências externas).

## Licença

Este projeto está sob a **CC0 1.0 Universal** (dedicação ao domínio público).
Você pode usar, copiar, modificar e distribuir o código livremente, para
qualquer finalidade, **sem qualquer obrigação de atribuição ou menção**.

Veja o texto integral em [`LICENSE`](./LICENSE).
