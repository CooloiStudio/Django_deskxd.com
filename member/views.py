from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from member.models import *
from home.models import *
from django.http import Http404

class IndexViews(generic.View):
    templates_file = 'MemberIndex.html'

    def get(self, request):

        if 'lang' in request.GET and request.GET['lang']:
            lang = request.GET['lang']
        else:
            lang = "zh-cn"


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        members = list(Member.objects.all())
        if members:
            members_list = []
            for p in members:
                minfos = list(MemberInfo.objects.filter(language=dlang, member=p.id))
                if minfos:
                    for m in minfos:
                        a = {'name': m.name, 'img': p.img, 'url': p.url, 'signature': m.signature}
                        members_list.append(a)
                else:
                    a = {'name': "", 'img': p.img, 'url': p.url, 'signature': ""}
                    members_list.append(a)
        else:
            members_list = []


        menus = list(Menu.objects.all().order_by('code'))
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


        contacts = list(Contact.objects.all().order_by('code'))
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


        sections = list(MSection.objects.all().order_by('code'))
        if sections:
            section_list = []
            for p in sections:
                sectioninfos = list(MSectionInfo.objects.filter(language=dlang, section=p.id))
                if sectioninfos:
                    for q in sectioninfos:
                        a = {"basepage": p.basepage, "name": q.name, "title": q.title, "subtitle":q.subtitle}
                        section_list.append(a)
                else:
                    a = {"basepage": p.basepage, "name": "", "title": "", "subtitle": ""}
                    section_list.append(a)
        else:
            section_list = []


        context = {
            'members_list': members_list,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
            "contact_list": contact_list,
            "section_list": section_list
        }
        return render(request,
                      self.templates_file,
                      context)