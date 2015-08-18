from django.shortcuts import render
from django.views import generic


class IndexView(generic.View):
    templates_file = 'Index.html'

    def get(self, request):
        context = {

        }
        return render(request,
                      self.templates_file,
                      context)