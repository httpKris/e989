from django.shortcuts import render
from .models import Article, File
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def listArticles(request):
    listArticlesObject = Article.objects.order_by('-pub_data')[:4]
    context = {
        'listArticlesObject': listArticlesObject
    }
    return render(request, 'article/list.html', context)


def detail(request, article_id):
    try:
        article_id = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')
    context = {
        'article': article_id
    }
    lastest_comments_list = article_id.comment_set.order_by('-id')[:5]

    return render(request, 'article/detail.html', {'article': article_id, 'lastest_comments_list': lastest_comments_list})


def live_comment(request, article_id):
    try:
        article_id = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    article_id.comment_set.create(
        autor_name=request.POST['name'], comments_text=request.POST['text'])

    return HttpResponseRedirect(reverse('detail', args=(article_id.id,)))


def file_download(request):
    try:
        download_file = File.objects.order_by('-id')[:1]
    except:
        raise Http404('Файл не найден')

    context = {
        'download_file': download_file
    }
    return render(request, 'article/price.html', context)
