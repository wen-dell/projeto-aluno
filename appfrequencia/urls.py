from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
    url(r'^frequencia/nova/$', views.frequencia, name="frequencia"),
    url(r'^login/', login, {'template_name':'utils/login.html', 'redirect_field_name':'home'},name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'},name='logout'),
    url(r'^turmas/$', views.turmas, name="turmas"),
    url(r'^turmas/tsi/$', views.tsi_listar, name="tsi_listar"),
    url(r'^turmas/meca/$', views.meca_listar, name="meca_listar"),
    url(r'^turmas/info/$', views.info_listar, name="info_listar"),
    url(r'^frequencia/aluno/$', views.frequencia_por_aluno, name="frequencia_por_aluno"),
    url(r'^frequencia/turma/$', views.frequencia_por_turma, name="frequencia_por_turma"),
]