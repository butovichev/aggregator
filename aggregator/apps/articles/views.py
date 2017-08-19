from django.views.generic import View
from django.shortcuts import render
# from django.utils import timezone
# from django.http import HttpResponse, Http404, HttpResponseForbidden

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article


class Articles(View):
    template_name = 'articles.html'

    def get(self, request):
        data = self.get_data(request.city)
        return render(request, self.template_name, {'posts': data})

    def get_data(city):
        articles = Article.objects.filter(city__domain_name=city)
        return articles

