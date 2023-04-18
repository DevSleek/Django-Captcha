from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm
from .models import Comment
from django.contrib import messages


def home(request):
    form = CommentForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        user = request.POST.get('user')
        content = request.POST.get('content')
        comment = Comment.objects.create(user=user, content=content)
        comment.save()
        return HttpResponse("<h2 style='color: rgba(22, 150, 50, 1)'> Success!")
    context = {
        'form': form
        }
    return render(request, 'home.html', context)