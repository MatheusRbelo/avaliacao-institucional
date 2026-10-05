from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from alunos.models import Aluno
from disciplinas.models import Disciplina


class Avaliacao(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('RESPONDIDA', 'Respondida'),
    ]

    nota = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comentario = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Relacionamento 1:N: um aluno faz varias avaliacoes, mas cada avaliacao
    # pertence a um unico aluno. Por isso a chave fica aqui, no lado N, e nao
    # no model Aluno: se ficasse la, cada aluno so poderia avaliar uma vez.
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes')

    # Relacionamento 1:N: uma disciplina recebe varias avaliacoes, mas cada
    # avaliacao fala de uma unica disciplina. Mesmo motivo: a chave estrangeira
    # fica no lado que se repete.
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'

    def __str__(self):
        return f'{self.aluno.nome} - {self.disciplina.codigo} ({self.status})'
