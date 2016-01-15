from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from gist.models import *
from django.contrib.auth.models import *

import os
import codecs

class IndexViews(generic.View):
    templates_file = 'gist.html'

    def get(self, request):

        if request.user.is_authenticated():
            users = list(User.objects.filter(username=request.user))
            if users.pop().is_superuser:
                perm = 1
                print perm
            else:
                perm = 0
                print perm
        else:
            perm = 0
            print "else" + str(perm)

        categorys = list(Category.objects.all())
        if categorys:
            category_list = []
            for p in categorys:
                posts = list(Post.objects.filter(category=p.id))
                if posts:
                    post_list = []
                    for post in posts:
                        a = {'id': post.id, 'title': post.title, 'date': post.date}
                        post_list.append(a)
                    b = {'categorys': p.name, 'post': post_list}
                else:
                    b = {'categorys': p.name, 'post': []}
                category_list.append(b)
        else:
            category_list = []

        context = {
            'category_list': category_list,
            'perm': perm
        }

        return render(request,
                      self.templates_file,
                      context)


class InfoViews(generic.View):
    templates_file = 'GistInfo.html'

    def get(self, request):

        if request.user.is_authenticated():
            users = list(User.objects.filter(username=request.user))
            if users.pop().is_superuser:
                perm = 1
            else:
                perm = 0
        else:
            perm = 0

        if 'code' in request.GET and request.GET['code']:
            postid = int(request.GET['code'])
            posts = list(Post.objects.filter(id=postid))
            if posts:
                post_list = []
                for post in posts:
                    a = {'category': post.category.name, 'title': post.title, 'url': post.url, 'date': post.date}
                    post_list.append(a)
            else:
                post_list = []
        else:
            postid = ""
            post_list = []


        context = {
            'post_list': post_list,
            'postid': postid,
            'perm': perm,
        }

        return render(request,
                      self.templates_file,
                      context)


class PostViews(generic.View):
    templates_file = 'post.html'

    def get(self, request):

        if not request.user.is_authenticated():
            return HttpResponseRedirect('/gist')

        category_list = list(Category.objects.all())

        context = {
            'category_list': category_list
        }

        return render(request,
                      self.templates_file,
                      context)


def create(request):

    if 'category' in request.POST and request.POST['category']:
        category = request.POST['category']
        categorys = list(Category.objects.filter(id=category)).pop()
    else:
        return HttpResponse("category is error")

    if 'title' in request.POST and request.POST['title']:
        title = request.POST['title']
    else:
        return HttpResponse("title is error")

    if 'postbody' in request.POST and request.POST['postbody']:
        postbody = request.POST['postbody']
    else:
        return HttpResponse("postbody is error")

    path = os.path.dirname(__file__) + '/../static/editor/file/'

    with codecs.open(path + title + '.md', 'w', 'utf-8') as content:
        content.write(postbody)

    url = 'editor/file/' + title + '.md'

    post = Post(
        category=categorys,
        title=title,
        url=url
    )
    post.save()

    return HttpResponseRedirect('/gist/info/?code=' + str(post.id))


def update(request):

    if 'postbody' in request.POST and request.POST['postbody']:
        postbody = request.POST['postbody']
    else:
        return HttpResponse("postbody is error")

    if 'postpath' in request.POST and request.POST['postpath']:
        postpath = request.POST['postpath']
    else:
        return HttpResponse("postpath is error")

    if 'postid' in request.POST and request.POST['postid']:
        postid = request.POST['postid']
    else:
        return HttpResponse("postid is error")

    path = os.path.dirname(__file__) + '/../static/' + postpath

    with codecs.open(path, 'w', 'utf-8') as content:
        content.write(postbody)

    return HttpResponseRedirect("/gist/info/?code=" + str(postid))

