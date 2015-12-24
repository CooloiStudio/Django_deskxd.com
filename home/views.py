from django.shortcuts import render, render_to_response
from django.views import generic
from home.models import *
from game.models import *
from information.models import *
from member.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
import random


class IndexViews(generic.View):
    templates_file = 'Index.html'

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


        introduceimages = list(IntroduceImage.objects.all().order_by("sort"))
        if introduceimages:
            introduce_list = []
            for p in introduceimages:
                infos = list(IntroduceInfo.objects.filter(language=dlang, image=p.id))
                if infos:
                    a = {"url": p.url, "img": p.img, "name": infos.pop().name}
                else:
                    a = {"url": p.url, "img": p.img, "name": ""}
                introduce_list.append(a)
        else:
            introduce_list = []


        games = list(Games.objects.all())
        if games:
            game_list = []
            for p in games:
                ginfos = list(GameInfo.objects.filter(language=dlang, games=p.id))
                if ginfos:
                    for q in ginfos:
                        a = {"img": p.img, "url": p.url, "name": q.name, "abstract": q.abstract}
                        game_list.append(a)
                else:
                    a = {"img": p.img, "url": p.url, "name": "", "abstract": ""}
                    game_list.append(a)
        else:
            game_list = []



        members = list(Member.objects.all())
        if members:
            random.shuffle(members)
            i = 4
            members_list = []
            for p in members:
                if 0 >= i:
                    break
                minfos = list(MemberInfo.objects.filter(language=dlang, member=p.id))
                if minfos:
                    for m in minfos:
                        a = {'name': m.name, 'img': p.img, 'url': p.url, 'signature': m.signature}
                        members_list.append(a)
                else:
                    a = {'name': "", 'img': p.img, 'url': p.url, 'signature': ""}
                    members_list.append(a)
                i = i - 1
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


        informations = list(Information.objects.all().order_by('sort'))
        if informations:
            i = 3
            info_list = []
            for p in informations:
                if 0 >= i:
                    break
                infoinfos = list(InformationInfo.objects.filter(language=dlang, infos=p.id))
                if infoinfos:
                    a = {'img': p.img, 'name': infoinfos.pop().name}
                else:
                    a = {'img': p.img, 'name': ""}
                info_list.append(a)
                i = i - 1
        else:
            info_list = []


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


        sections = list(Section.objects.all().order_by('sort'))
        if sections:
            section_list = []
            for p in sections:
                sectioninfos = list(SectionInfo.objects.filter(language=dlang, section=p.id))
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
            'game_list': game_list,
            'members_list': members_list,
            'introduce_list': introduce_list,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
            'info_list': info_list,
            "contact_list": contact_list,
            "section_list": section_list
        }
        return render_to_response(
                self.templates_file,
                context,
                context_instance=RequestContext(request))