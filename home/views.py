from django.shortcuts import render
from django.views import generic
from home.models import *
from game.models import *
from information.models import *
from member.models import *
from django.http import HttpResponse, HttpResponseRedirect
import random


class IndexViews(generic.View):
    templates_file = 'Index.html'

    def get(self, request):

        introduceimages = list(IntroduceImage.objects.all().order_by("code"))
        if not introduceimages:
            introduceimages = []


        games = list(Games.objects.all())
        if not games:
            games = []

        # MEMBER
        members = list(Member.objects.all())

        random.shuffle(members)

        i = 4
        members_list = []
        for p in members:
            if 0 >= i:
                break;
            a = {'name': p.name, 'img': p.img, 'url': p.url, 'signature': p.signature}
            members_list.append(a)
            i = i - 1


        context = {
            'games': games,
            'members_list': members_list,
            'introduceimages': introduceimages,
        }
        return render(request,
                      self.templates_file,
                      context)