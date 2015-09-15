from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from contact.models import *

class IndexView(generic.View):
    templates_file = 'ContactIndex.html'

    def get(self, request):

        contacts = list(Contact.objects.all())
        if not contacts:
            contacts = []

        context = {
            'contacts': contacts
        }
        return render(request,
                      self.templates_file,
                      context)