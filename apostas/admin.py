from django.contrib import admin

# Register your models here.

from apostas.models import *

class TimeAdmin(admin.ModelAdmin):
    list_display = ['nome','cidade']


class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ['nome',]

class JogoAdmin(admin.ModelAdmin):
    list_display = ('campeonato','time1', 'time2','data_hora')

admin.site.register(Time, TimeAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(Jogo, JogoAdmin)
admin.site.register(Aposta)
