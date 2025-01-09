from rest_framework import serializers
from .models import Livro, Usuario, Emprestimo

class Livro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class Emprestimo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class Lista_Emprestimo_Livro_Serializer(serializers.ModelSerializer):
    livro = serializers.ReadOnlyField(source = 'livro.titulo')

    class Meta:
        model = Emprestimo
        fields = ['livro', 'status', 'dataDeEmprestimo', 'dataDeDevolucao']

class Lista_Emprestimo_Usuario_Serializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source = 'usuario.nome')

    class Meta:
        model = Emprestimo
        fields = ['usuario', 'status', 'dataDeEmprestimo', 'dataDeDevolucao']