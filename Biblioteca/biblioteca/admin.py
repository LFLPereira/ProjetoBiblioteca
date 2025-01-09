from django.contrib import admin
from.models import Livro, Usuario, Emprestimo

class Livro_Admin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'dataDePublicacao', 'isbn', 'descricao')
    list_display_links = ('titulo', 'autor')
    list_per_page = 10
    search_fields = ('titulo', 'autor', 'isbn')

admin.site.register(Livro, Livro_Admin)

class Usuario_Admin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'papel')
    list_display_links = ('nome', 'email')
    list_per_page = 10
    search_fields = ('nome', 'email', 'telefone')

admin.site.register(Usuario, Usuario_Admin)

class Emprestimo_Admin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'status', 'dataDeEmprestimo', 'dataDeDevolucao')
    list_display_links = ('livro', 'usuario')
    list_per_page = 10
    search_fields = ('livro', 'usuario')

admin.site.register(Emprestimo, Emprestimo_Admin)
