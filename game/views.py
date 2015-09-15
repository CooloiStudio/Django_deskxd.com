from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from game.models import *

class IndexView(generic.View):
    templates_file = 'GameIndex.html'

    def get(self, request):

        games = list(Games.objects.all().order_by("code"))
        if games:
            game_list = []
            for p in games:
                if p.code % 2 != 0:
                    a = {"name": p.name, "img": p.img, "url": p.url, "introduce": p.introduce, "group": 0}
                    game_list.append(a)
                else:
                    a = {"name": p.name, "img": p.img, "url": p.url, "introduce": p.introduce, "group": 1}
                    game_list.append(a)
        else:
            game_list = []

        context = {
            'game_list': game_list
        }
        return render(request,
                      self.templates_file,
                      context)