from django.shortcuts import render
from django.views import generic
from home.models import *
from django.http import HttpResponse, HttpResponseRedirect


class IndexView(generic.View):
    templates_file = 'Index.html'

    def get(self, request):

        introduceimages = list(IntroduceImage.objects.all().order_by("code"))
        if not introduceimages:
            introduceimages = []

        groups = list(Group.objects.all().order_by("code"))
        if groups:
            group_list = []
            for p in groups:
                groupinfos = list(GroupInfo.objects.filter(group=int(p.id)).order_by("code"))
                info_list = []
                for q in groupinfos:
                    a = {'image_url': q.image_url, 'url': q.url, 'title': q.title, 'value': q.value, 'info_class': q.info_class, 'info_id': q.info_id, 'txt_class': q.txt_class}
                    info_list.append(a)
                b = {'g_title': p.title, 'title_logo': p.title_logo, 'logo_color': p.logo_color, 'url': p.url, 'default': p.default, 'info_list': info_list}
                group_list.append(b)
        else:
            group_list = []

        context = {
            'introduceimages': introduceimages,
            'group_list': group_list,
        }
        return render(request,
                      self.templates_file,
                      context)