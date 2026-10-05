from django.db.models import Avg, Count
from django.http import JsonResponse
from .models import Avaliacao


def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().values()
    return JsonResponse(list(avaliacoes), safe=False)


def listar_pendentes(request):
    avaliacoes = Avaliacao.objects.filter(status='PENDENTE').values()
    return JsonResponse(list(avaliacoes), safe=False)


# Desafio extra: agrupa as avaliacoes por disciplina e calcula, para cada uma,
# a media das notas e o total de avaliacoes ja respondidas.
def resumo_por_disciplina(request):
    resumo = (
        Avaliacao.objects.filter(status='RESPONDIDA')
        .values('disciplina__nome', 'disciplina__codigo')
        .annotate(media_notas=Avg('nota'), total_respondidas=Count('id'))
        .order_by('disciplina__nome')
    )
    return JsonResponse(list(resumo), safe=False)
