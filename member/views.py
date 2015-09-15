from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from member.models import *

class IndexView(generic.View):
    templates_file = 'MemberIndex.html'

    def get(self, request):

        group_one = list(Members.objects.filter(group=1))
        if not group_one:
            group_one = []

        group_two = list(Members.objects.filter(group=2))
        if not group_two:
            group_two = []

        group_three = list(Members.objects.filter(group=3))
        if not group_three:
            group_three = []

        context = {
            'group_one': group_one,
            'group_two': group_two,
            'group_three': group_three
        }
        return render(request,
                      self.templates_file,
                      context)