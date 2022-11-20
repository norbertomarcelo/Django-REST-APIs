from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not nome_validator(data['nome']):
            raise serializers.ValidationError(
                {"nome": "Nao inclua numeros neste campo."})
        if not cpf_validadtors(data['cpf']):
            raise serializers.ValidationError(
                {"cpf": "Numero de CPF invalido."})
        if not rg_validator(data['rg']):
            raise serializers.ValidationError(
                {"rg": "O RG deve ter 9 digitos"})
        if not celular_validdator(data['celular']):
            raise serializers.ValidationError(
                {"celumar": "Numero de celular invalido"})
        return data
