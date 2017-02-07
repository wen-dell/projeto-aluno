from django.shortcuts import render, redirect
from .forms import FrequenciaForm
from django.contrib.auth.decorators import login_required
from .models import Aluno, Frequencia


@login_required(login_url="login")
def frequencia(request):
    if request.method == "POST":
        form = FrequenciaForm(request.POST)
        if form.is_valid():
            frequencia = form.save()
            frequencia.save()
            return redirect('home')
    else:
        form = FrequenciaForm()
    return render(request, 'frequencia.html', {'form' : form})

    form = FrequenciaForm()
    return render(request, "frequencia.html", {'form' : form})


@login_required(login_url="login")
def turmas(request):
    return render(request, 'turmas/turmas.html')


@login_required(login_url="login")
def home(request):
    return render(request, 'base.html')


@login_required(login_url="login")
def tsi_listar(request):
    alunos_tsi = Aluno.objects.filter(id_turma__id_turma=1)
    return render(request, 'turmas/tsi.html', {'alunos' : alunos_tsi})


@login_required(login_url="login")
def meca_listar(request):
    alunos_meca = Aluno.objects.filter(id_turma__id_turma=2)
    return render(request, 'turmas/meca.html', {'alunos' : alunos_meca})


@login_required(login_url="login")
def info_listar(request):
    alunos_info = Aluno.objects.filter(id_turma__id_turma=3)
    return render(request, 'turmas/info.html', {'alunos' : alunos_info})


@login_required(login_url="login")
def frequencia_por_aluno(request):
    frequencias = Frequencia.objects.all()
    return render(request, "frequencia_aluno.html", {'frequencias' : frequencias})


@login_required(login_url="login")
def frequencia_por_turma(request):
    alunos_tsi = Aluno.objects.filter(id_turma__id_turma=1)
    alunos_meca = Aluno.objects.filter(id_turma__id_turma=2)
    alunos_info = Aluno.objects.filter(id_turma__id_turma=3)
    frequencias = Frequencia.objects.all()

    faltas_tsi = []
    for aluno in alunos_tsi:
        faltou = False
        for frequencia in frequencias:
            if not faltou and str(aluno.matricula) == str(frequencia.matricula):
                faltas_tsi.append(frequencia.faltas)
                faltou = True
            elif faltou and str(aluno.matricula) == str(frequencia.matricula):
                faltas_tsi[-1] += frequencia.faltas
        if not faltou:
            faltas_tsi.append(0)


    faltas_meca = []
    for aluno in alunos_meca:
        faltou = False
        for frequencia in frequencias:
            if not faltou and str(aluno.matricula) == str(frequencia.matricula):
                faltas_meca.append(frequencia.faltas)
                faltou = True
            elif faltou and str(aluno.matricula) == str(frequencia.matricula):
                faltas_meca[-1] += frequencia.faltas
        if not faltou:
            faltas_meca.append(0)

    faltas_info = []
    for aluno in alunos_info:
        faltou = False
        for frequencia in frequencias:
            if not faltou and str(aluno.matricula) == str(frequencia.matricula):
                faltas_info.append(frequencia.faltas)
                faltou = True
            elif faltou and str(aluno.matricula) == str(frequencia.matricula):
                faltas_info[-1] += frequencia.faltas
        if not faltou:
            faltas_info.append(0)

    return render(request, "frequencia_turma.html", {'alunos_tsi' : alunos_tsi,
                                                     'alunos_meca' : alunos_meca,
                                                     'alunos_info' : alunos_info,
                                                     'frequencias' : frequencias,
                                                     'faltas_tsi' : faltas_tsi,
                                                     'faltas_info' : faltas_info,
                                                     'faltas_meca' : faltas_meca})
