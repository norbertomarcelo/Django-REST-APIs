import re
from validate_docbr import CPF


def cpf_validadtors(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)


def nome_validator(nome):
    return nome.isalpha()


def rg_validator(numero_do_rg):
    return len(numero_do_rg) == 9


def celular_validdator(numero_celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
