from django.shortcuts import render
from django.views import generic
from home.models import *
from game.models import *
from information.models import *
from member.models import *
from django.http import HttpResponse, HttpResponseRedirect
import random


class IndexView(generic.View):
    templates_file = 'Index.html'

    def get(self, request):

        introduceimages = list(IntroduceImage.objects.all().order_by("code"))
        if not introduceimages:
            introduceimages = []

        # GAME
        games = list(Games.objects.all().order_by("code"))
        if games:
            games_list = random.sample(games, 2)
            i = 2
            while i > 0:
                game_list = []
                for p in games_list:
                    if i > 1:
                        a = {'name': p.name, 'img': p.img, 'url': p.url, 'abstract': p.abstract, 'i': 1}
                    else:
                        a = {'name': p.name, 'img': p.img, 'url': p.url, 'abstract': p.abstract, 'i': 0}
                    game_list.append(a)
                    i = i - 1
        else:
            game_list = []

        # INFORMATION
        infos = list(Information.objects.all().order_by("code"))
        if infos:
            i = 3
            while i > 0:
                info_list = []
                for q in infos:
                    if i > 1:
                        b = {'img': q.img, 'name': q.name, 'i': 1}
                    else:
                        b = {'img': q.img, 'name': q.name, 'i': 0}
                    info_list.append(b)
                    i = i - 1
        else:
            info_list = []

        # MEMBER
        members = list(Member.objects.all())
        if members:
            members_list = random.sample(members, 4)
            i = 4
            while i > 0:
                member_list = []
                for m in members_list:
                    if i > 1:
                        c = {'name': m.name, 'img': m.img, 'url': m.url, 'signature': m.signature, 'i': 1}
                    else:
                        c = {'name': m.name, 'img': m.img, 'url': m.url, 'signature': m.signature, 'i': 0}
                    member_list.append(c)
                    i = i - 1
        else:
            member_list = []

        context = {
            'introduceimages': introduceimages,
            'game_list': game_list,
            'info_list': info_list,
            'member_list': member_list
        }
        return render(request,
                      self.templates_file,
                      context)