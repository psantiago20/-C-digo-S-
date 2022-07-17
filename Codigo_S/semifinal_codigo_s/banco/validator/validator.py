import re


def valida_cpf(cpf):
    """Verifica se o campo CPF tem 11 caracteres"""
    return not re.match(r"^([\s\d]+)$", cpf)


def valida_cnpj(cnpj):
    """Verifica se o campo CNPJ tem 14 caracteres"""
    return len(str(cnpj)) == 14
