from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from member.models import *

class IndexView(generic.View):
    templates_file = 'MemberIndex.html'

    def get(self, request):

        members = list(Member.objects.all())
        if not members:
            members = []

        context = {
            'members': members
        }
        return render(request,
                      self.templates_file,
                      context)