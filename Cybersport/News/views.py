from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import NewsForm


def news_list(request):
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news, "title": "EsportZP", "title2": "Новости CyberSport",
                                                   })


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})


def news_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {
                     'news': news, 'categories': categories,
    })


def news_add(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add.html', {'form': form})

