from biblioteca.views import Livro_viewSet, Usuario_viewSet, Emprestimo_viewSet, Emprestimo_Lista_Livro, Emprestimo_Lista_Usuario
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livros', Livro_viewSet, basename = 'livros')
router.register('usuarios', Usuario_viewSet, basename = 'usuarios')
router.register('emprestimos', Emprestimo_viewSet, basename = 'emprestimos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('emprestimos/livros/<int:pk>/', Emprestimo_Lista_Livro.as_view(), name='emprestimo_livro'),
    path('emprestimos/usuarios/<int:pk>/', Emprestimo_Lista_Usuario.as_view(), name='emprestimo_usuario'),
]
