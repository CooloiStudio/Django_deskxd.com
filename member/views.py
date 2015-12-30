from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from member.models import *
from home.models import *
from django.http import Http404
import re

class IndexViews(generic.View):
    templates_file = 'MemberIndex.html'

    def get(self, request):

        lang = request.LANGUAGE_CODE


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        groups = list(Group.objects.all().order_by('sort'))
        if groups:
            members_list = []
            for q in groups:
                members = list(Member.objects.filter(group=q.id))
                if members:
                    g_list = []
                    for p in members:
                        minfos = list(MemberInfo.objects.filter(language=dlang, member=p.id))
                        if minfos:
                            for m in minfos:
                                if re.match('[a-zA-z]+://[^\s]*', p.img):
                                    a = {'name': m.name, 'img': p.img, 'url': p.url, 'signature': m.signature}
                                else:
                                    a = {'name': m.name, 'img': "", 'url': p.url, 'signature': m.signature}
                                g_list.append(a)
                        else:
                            if re.match('[a-zA-z]+://[^\s]*', p.img):
                                a = {'name': "", 'img': p.img, 'url': p.url, 'signature': ""}
                            else:
                                a = {'name': "", 'img': "", 'url': p.url, 'signature': ""}
                            g_list.append(a)
                else:
                    g_list = []
                b = {"group": q.name, "members": g_list}
                members_list.append(b)
        else:
            members_list = []


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
            qr_list = []
            c_list = []
            for p in contacts:
                cinfos = list(ContactInfo.objects.filter(language=dlang, contact=p.id))
                if cinfos:
                    if p.code == "QR":
                        for q in cinfos:
                            qr = q.img
                            qr_list.append(qr)
                    else:
                        cinfo_list = []
                        for q in cinfos:
                            b = {"text": q.text, "img": q.img, "url": q.url,}
                            cinfo_list.append(b)
                        for m in cinfos:
                            if m.name == a["name"]:
                                break
                            a = {"remark": p.remark, "code": p.code, "name": m.name, "info": cinfo_list}
                            c_list.append(a)
                else:
                    if p.code == "QR":
                        qr = ""
                        qr_list.append(qr)
                    else:
                        a = {"remark": p.remark, "code": p.code, "name": "", "info": []}
                        c_list.append(a)

            def group_list(l, block):
                size = len(l)
                return [l[i:i+block] for i in range(0, size, block)]

            contact_list = group_list(c_list, 2)
            print qr_list, contact_list
        else:
            contact_list = []
            qr_list = []


        sections = list(MSection.objects.all().order_by('sort'))
        if sections:
            section_list = []
            for p in sections:
                sectioninfos = list(MSectionInfo.objects.filter(language=dlang, section=p.id))
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
            'members_list': members_list,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
            "contact_list": contact_list,
            "section_list": section_list,
            'qr_list': qr_list
        }
        return render(request,
                      self.templates_file,
                      context)