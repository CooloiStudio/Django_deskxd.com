from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from thanks.models import *
from home.models import *
from django.http import Http404
import random

class IndexViews(generic.View):
    templates_file = 'thanksIndex.html'

    def get(self, request):

        thankss = list(Thanks.objects.all())
        if thankss:
            random.shuffle(thankss)
        else:
            thankss = []

        lang = request.LANGUAGE_CODE


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        menus = list(Menu.objects.all().order_by('sort'))
        if menus:
            menu_list = []
            for p in menus:
                menuinfos = list(MenuInfo.objects.filter(language=dlang, menu=p.id))
                if menuinfos:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                else:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                menu_list.append(a)
        else:
            menu_list = []


        contacts = list(Contact.objects.all().order_by('sort'))
        if contacts:
            c_list = []
            for p in contacts:
                cinfos = list(ContactInfo.objects.filter(language=dlang, contact=p.id))
                if cinfos:
                    for q in cinfos:
                        a = {"remark": p.remark, "name": q.name, "text": q.text}
                        c_list.append(a)
                else:
                    a = {"remark": p.remark, "name": "", "text": ""}
                    c_list.append(a)

            def group_list(l, block):
                size = len(l)
                return [l[i:i+block] for i in range(0, size, block)]

            contact_list = group_list(c_list, 2)
        else:
            contact_list = []


        sections = list(TSection.objects.all().order_by('sort'))
        if sections:
            section_list = []
            for p in sections:
                sectioninfos = list(TSectionInfo.objects.filter(language=dlang, section=p.id))
                if sectioninfos:
                    for q in sectioninfos:
                        a = {"basepage": p.basepage.name, "name": q.name, "title": q.title, "subtitle":q.subtitle}
                        section_list.append(a)
                else:
                    a = {"basepage": p.basepage.name, "name": "", "title": "", "subtitle": ""}
                    section_list.append(a)
        else:
            section_list = []


        context = {
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
            "contact_list": contact_list,
            "section_list": section_list,
            'thankss': thankss,
        }

        return render(request,
                      self.templates_file,
                      context)