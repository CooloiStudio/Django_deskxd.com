from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from game.models import *

class IndexView(generic.View):
    templates_file = 'GameIndex.html'

    def get(self, request):

        games = list(Games.objects.all().order_by("code"))

        context = {
            'games': games
        }
        return render(request,
                      self.templates_file,
                      context)