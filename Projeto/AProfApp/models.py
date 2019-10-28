from django.db import models

# Create your models here.


class Turma (models.Model):
  data_inicio = models.DateField('Data de início')
  data_termino = models.DateField('Data de termino')
  hora_inicio = models.TimeField('Começa à(s)')
  hora_final = models.TimeField('Termina à(s)')
  professor = models.ForeignKey('Professor', on_delete=models.CASCADE)

  def __str__(self):
      return "Turma do(a) professor(a) " + (str(self.professor))

class Curso (models.Model):
  nome = models.CharField('Nome', max_length = 100)
  carga_horaria = models.SmallIntegerField('Carga horária')
  emenda = models.TextField('Emenda do curso')
  valor = models.PositiveIntegerField('Valor(R$)')

  def __str__(self):
      return self.nome

class Professor (models.Model):
  nome = models.CharField('Nome' ,max_length = 50)
  telefone = models.IntegerField('Telefone')
  valor_hora_aula = models.PositiveIntegerField('Valor da hora aula (R$)')
  curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
  class Meta:
      verbose_name_plural = 'professores'
  def __str__(self):
      return self.nome