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

        if request.user.is_authenticated() and request.user.has_perm('gist.can_post'):
            perm = 1
        else:
            perm = 0

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
    templates_file = 'content.html'

    def get(self, request):

        if request.user.is_authenticated() and request.user.has_perm('gist.can_post'):
            perm = 1
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


class UpdateInfoViews(generic.View):
    templates_file = 'update.html'

    def get(self, request):

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


        if not (request.user.is_authenticated() and request.user.has_perm('gist.can_post')):
            return HttpResponseRedirect('/gist/info/?code=' + str(postid))


        context = {
            'post_list': post_list,
            'postid': postid,
        }

        return render(request,
                      self.templates_file,
                      context)


class PostViews(generic.View):
    templates_file = 'edit/post.html'

    def get(self, request):

        if not request.user.is_authenticated():
            return HttpResponseRedirect('/gist')
        else:
            if not request.user.has_perm('gist.can_post'):
                return HttpResponseRedirect('/gist')

        category_list = list(Category.objects.all())

        context = {
            'category_list': category_list
        }

        return render(request,
                      self.templates_file,
                      context)


class GroupViews(generic.View):
    templates_file = 'edit/group.html'

    def get(self, request):

        if not request.user.is_authenticated():
            return HttpResponseRedirect('/gist')
        else:
            if not request.user.has_perm('gist.can_post'):
                return HttpResponseRedirect('/gist')

        context = {}

        return render(request,
                      self.templates_file,
                      context)


def create_group(request):

    if 'category' in request.POST and request.POST['category']:
        category = request.POST['category']
    else:
        return HttpResponse("category is error")

    p = Category(name=category)
    p.save()

    return HttpResponseRedirect('/gist/post')


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

    post = Post(
        category=categorys,
        title=title,
    )
    post.save()

    path = os.path.dirname(__file__) + '/../static/editor/file/'

    with codecs.open(path + 'editor_' + str(post.id) + '.md', 'w', 'utf-8') as content:
        content.write(postbody)

    url = 'editor/file/' + 'editor_' + str(post.id) + '.md'

    uppost = Post.objects.filter(id=post.id)
    for p in uppost:
        p.url = url
        p.save()

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

