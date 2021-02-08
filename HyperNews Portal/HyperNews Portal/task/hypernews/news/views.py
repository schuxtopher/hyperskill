from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import View
import json
import random
from datetime import datetime


# Create your views here.
class NewsView(View):
    def get(self, request,  *args, **kwargs):
        return redirect("/news/")


class MainPageView(View):
    def get(self, request,  *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            articles = json.load(json_file)

        if 'q' in request.GET:
            if request.GET['q'] != '':
                title = request.GET['q']
                articles = [a for a in articles if title in a['title']]

        dates = [article['created'].split()[0] for article in articles]
        dates.sort(reverse=True)
        dates = dict.fromkeys(dates)

        for article in articles:
            article['created'] = article['created'].split()[0]

        context = {'dates': dates, 'articles': articles}
        return render(request, "mainPage/mainPage.html", context=context)


class ArticleView(View):
    def get(self, request, article_id,  *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            articles = json.load(json_file)

        valid_ids = [str(article['link']) for article in articles]
        if article_id not in valid_ids:
            raise Http404

        articles_link = {str(article['link']): article for article in articles}
        context = {"article": articles_link[article_id]}
        return render(request, "article/article.html", context=context)


class CreateView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, "create/create.html")

    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            articles = json.load(json_file)

        article = dict()
        article['created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        article['title'] = request.POST.get('title')
        article['text'] = request.POST.get('text')

        used_ids = [str(article['link']) for article in articles]
        while True:
            link = random.randint(0, 999999999)
            if link not in used_ids:
                break
        article['link'] = link

        articles.append(article)

        with open(settings.NEWS_JSON_PATH, "w") as json_file:
            json.dump(articles, json_file)

        return redirect('../')


