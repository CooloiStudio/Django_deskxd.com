from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from information.models import *

class IndexViews(generic.View):
    templates_file = 'InformationIndex.html'

    def get(self, request):

        infos = list(Information.objects.all().order_by("code"))
        if not infos:
            infos = []

        context = {
            'infos': infos
        }
        return render(request,
                      self.templates_file,
                      context)