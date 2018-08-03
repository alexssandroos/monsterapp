from django.db import models

# Create your models here.
class Pessoa(models.Model):
	class Meta:
		abstract = True

	MASC = 'M'
	FEM = 'F'
	OPCOES	= (
		(MASC, 'Masculino'),
		(FEM, 'Feminino')
	)

	nome = models.CharField(max_length=150)
	data_nascimento = models.DateField()
	endereco = models.CharField(max_length=100)
	telefone = models.CharField(max_length=11)
	sexo  = models.CharField(max_length=1, choices=OPCOES)

class Aluno(Pessoa):
	data_cadastro = models.DateField()

	def __str__(self):
		return f'{self.nome} - {self.telefone}'

class Instrutor(Pessoa):
	def __str__(self):
		return f'Instrutor : {self.nome}'