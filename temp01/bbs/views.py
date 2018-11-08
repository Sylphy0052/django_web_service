from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Thread

class IndexView(generic.ListView):
    template_name = 'bbs/index.html'
    context_object_name = 'latest_thread_list'

    def get_queryset(self):
        return Thread.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Thread
    template_name = 'bbs/thread_list.html'

    def get_queryset(self):
        return Thread.objects.filter(
            pub_date__lte=timezone.now()
        )
