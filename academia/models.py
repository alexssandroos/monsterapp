from django.db import models

# Create your models here.
class Modalidade(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome


class Turma(models.Model):
	horario = models.CharField(max_length=100)
	modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.modalidade} - {self.horario}'
