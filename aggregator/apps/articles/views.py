from django.views.generic import View
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404, HttpResponseForbidden

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return HttpResponse("aggregator")

