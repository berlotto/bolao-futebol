from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255,blank=True)
    simbolo = models.ImageField(upload_to="simbolos",blank=True)

    def __unicode__(self):
        return self.nome


class Campeonato(models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255,blank=True)
    imagem = models.ImageField(upload_to="campeonatos",blank=True)

    def __unicode__(self):
        return self.nome


class Jogo(models.Model):
    campeonato = models.ForeignKey('Campeonato',related_name="jogos")
    time1 = models.ForeignKey('Time', related_name="jogos_mandante")
    time2 = models.ForeignKey('Time', related_name="jogos_visitante")
    data_hora = models.DateTimeField()
    gols_time1 = models.PositiveSmallIntegerField(blank=True,null=True)
    gols_time2 = models.PositiveSmallIntegerField(blank=True,null=True)
    estadio = models.CharField(max_length=255)
    cidade_estado = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s x %s" % (self.time1.nome, self.time2.nome)


class Aposta(models.Model):
    jogo = models.ForeignKey('Jogo', related_name="apostas")
    gols_time1 = models.PositiveSmallIntegerField(blank=True,null=True)
    gols_time2 = models.PositiveSmallIntegerField(blank=True,null=True)
    user = models.ForeignKey(User)
