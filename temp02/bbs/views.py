# from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewThreadForm
from .models import Bbs, Thread, Post

def home(request):
    bbss = Bbs.objects.all()
    return render(request, 'home.html', {'bbss': bbss})

def bbs_threads(request, pk):
    bbs = get_object_or_404(Bbs, pk=pk)
    return render(request, 'threads.html', {'bbs': bbs})

def new_thread(request, pk):
    bbs = get_object_or_404(Bbs, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.bbs = bbs
            thread.starter = user
            thread.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                thread=thread,
                created_by=user
            )
            return redirect('bbs:bbs_threads', pk=bbs.pk)
    else:
        form = NewThreadForm()

    return render(request, 'new_thread.html', {'bbs': bbs, 'form': form})
