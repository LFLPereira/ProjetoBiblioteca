from .serializers import Livro_Serializer, Usuario_Serializer, Emprestimo_Serializer, Lista_Emprestimo_Livro_Serializer, Lista_Emprestimo_Usuario_Serializer
from .models import Livro, Usuario, Emprestimo
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Livro_viewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Livro_Serializer

    def get_queryset(self):
        queryset = Livro.objects.all()
        titulo = self.request.query_params.get('titulo')
        autor = self.request.query_params.get('autor')
        if titulo:
            queryset = queryset.filter(titulo=titulo)
        if autor:
            queryset = queryset.filter(autor=autor)
        return queryset

class Usuario_viewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Usuario_Serializer

    def get_queryset(self):
        queryset = Usuario.objects.all()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome=nome)
        return queryset

class Emprestimo_viewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Emprestimo.objects.all()
    serializer_class = Emprestimo_Serializer

class Emprestimo_Lista_Livro(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(livro_id = self.kwargs['pk'])

        return queryset
    
    serializer_class = Lista_Emprestimo_Livro_Serializer

class Emprestimo_Lista_Usuario(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(usuario_id = self.kwargs['pk'])

        return queryset
    
    serializer_class = Lista_Emprestimo_Usuario_Serializer