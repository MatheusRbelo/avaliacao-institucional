from django.http import JsonResponse
from .models import Aluno


def listar_alunos(request):
    alunos = Aluno.objects.all().values()
    return JsonResponse(list(alunos), safe=False)
