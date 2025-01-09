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
    status = serializers.SerializerMethodField()
    dataDeEmprestimo = serializers.SerializerMethodField()
    dataDeDevolucao = serializers.SerializerMethodField()

    class Meta:
        model = Emprestimo
        fields = ['curso', 'status', 'dataDeEmprestimo', 'dataDeDevolucao']

    def get_status(self, obj):
        return obj.get_status_display()
    
    def get_dataDeEmprestimo(self, obj):
        return obj.get_dataDeEmprestimo_display()

    def get_dataDeDevolucao(self, obj):
        return obj.get_dataDeDevolucao_display()

class Lista_Emprestimo_Usuario_Serializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source = 'usuario.nome')
    status = serializers.SerializerMethodField()
    dataDeEmprestimo = serializers.SerializerMethodField()
    dataDeDevolucao = serializers.SerializerMethodField()

    class Meta:
        model = Emprestimo
        fields = ['usuario', 'status', 'dataDeEmprestimo', 'dataDeDevolucao']

    def get_status(self, obj):
        return obj.get_status_display()
    
    def get_dataDeEmprestimo(self, obj):
        return obj.get_dataDeEmprestimo_display()

    def get_dataDeDevolucao(self, obj):
        return obj.get_dataDeDevolucao_display()