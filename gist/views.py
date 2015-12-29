from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from gist.models import *
from markdown import markdown


class IndexViews(generic.View):
    templates_file = 'gist.html'

    def get(self, request):

        categorys = list(Category.objects.all())
        if categorys:
            category_list = []
            for p in categorys:
                posts = list(Post.objects.filter(category=p.id))
                if posts:
                    post_list = []
                    for post in posts:
                        body = markdown(post.body)
                        a = {'id': post.id, 'title': post.title, 'body': body, 'date': post.date}
                        post_list.append(a)
                    b = {'categorys': p.name, 'post': post_list}
                else:
                    b = {'categorys': p.name, 'post': []}
                category_list.append(b)
        else:
            category_list = []

        context = {
            'category_list': category_list
        }

        return render(request,
                      self.templates_file,
                      context)


class InfoViews(generic.View):
    templates_file = 'GistInfo.html'

    def get(self, request):

        if 'code' in request.GET and request.GET['code']:
            postid = int(request.GET['code'])
            posts = list(Post.objects.filter(id=postid))
            if posts:
                post_list = []
                for post in posts:
                    body = markdown(post.body)
                    a = {'category': post.category.name, 'title': post.title, 'body': body, 'date': post.date}
                    post_list.append(a)
            else:
                post_list = []
        else:
            postid = ""


        context = {
            'post_list': post_list,
            'postid': postid,
        }

        return render(request,
                      self.templates_file,
                      context)