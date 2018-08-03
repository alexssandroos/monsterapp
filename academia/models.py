from django.db import models
from pessoa.models import Instrutor, Aluno


class Modalidade(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome


class Horario(models.Model):
	descricao = models.CharField(max_length=100)
	modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
	ativo = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.modalidade.nome} - {self.descricao}'


class Turma(models.Model):
	horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
	instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
	alunos = models.ManyToManyField(Aluno)
	limite_alunos = models.IntegerField()
	valor_mensalidade = models.DecimalField(max_digits=5,decimal_places=2)
	valor_diaria = models.DecimalField(max_digits=5,decimal_places=2)

	def __str__(self):
		return f'{self.instrutor.nome} - {self.horario.modalidade.nome} : {self.horario.descricao}'


		
