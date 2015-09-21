from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from game.models import *

class IndexView(generic.View):
    templates_file = 'GameIndex.html'

    def get(self, request):

        games = list(Games.objects.all().order_by("code"))
        if not games:
            games = []

        gameimgs = list(GameImages.objects.all())
        if not gameimgs:
            gameimgs = []

        context = {
            'games': games,
            'gameimgs': gameimgs
        }
        return render(request,
                      self.templates_file,
                      context)