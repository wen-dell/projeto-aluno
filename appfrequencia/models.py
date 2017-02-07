from django.db import models


class Turma(models.Model):
    id_turma = models.IntegerField()
    nome = models.CharField(max_length=20)
    horario = models.TimeField()
    data_inicio = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    matricula = models.IntegerField(default=0)
    nome = models.CharField(max_length=60)

    def __str__(self):
        return str(self.matricula)


class Frequencia(models.Model):
    matricula = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_com_hora = models.DateTimeField(auto_now=True)
    faltas = models.IntegerField(default=0)

    def __str__(self):
        return str(self.data_com_hora)




