from django.db import models

class Livro(models.Model):
    titulo = models.CharField(blank=False, max_length=255)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    dataDePublicacao = models.DateField()
    isbn = models.CharField(blank=False, max_length=13)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    PAPEL = (
        ('A', "Administrador"),
        ('L', "Leitor"),
    )
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    telefone = models.CharField(max_length=14)
    papel = models.CharField(max_length=1, choices= PAPEL, blank=False, null=False, default='A')

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    dataDeEmprestimo = models.DateField()
    dataDeDevolucao = models.DateField()
