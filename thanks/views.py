from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from thanks.models import *
import random

class IndexView(generic.View):
    templates_file = 'thanksIndex.html'

    def get(self, request):

        thankss = list(Thanks.objects.all())
        if thankss:
            random.shuffle(thankss)
        else:
            thankss = []

        context = {
            'thankss': thankss,
        }
        return render(request,
                      self.templates_file,
                      context)