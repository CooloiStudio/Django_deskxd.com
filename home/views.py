from django.shortcuts import render
from django.views import generic
from home.models import *
from game.models import *
from information.models import *
from member.models import *
from django.http import HttpResponse, HttpResponseRedirect
import random


class IndexView(generic.View):
    templates_file = 'index.html'

    def get(self, request):

        introduceimages = list(IntroduceImage.objects.all().order_by("code"))
        if not introduceimages:
            introduceimages = []


        games = list(Games.objects.all())
        if not games:
            games = []

        # MEMBER
        members = list(Member.objects.all())
        members = members[:2]

        random.shuffle(members)

        i=4
        members_list = []
        for p in members:
            if 0 >= i:
                break;
            members_list.append(p.code)
            i = i - 1


        print members_list

        context = {
            'games': games,
            'members_list': members_list,
            'introduceimages': introduceimages
        }
        return render(request,
                      self.templates_file,
                      context)