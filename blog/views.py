from django.shortcuts import render
from .models import RegistroRescatados
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = RegistroRescatados.objects.filter(Estado='D')
    return render(request, 'blog/post_list.htm', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(RegistroRescatados, pk=pk)
    return render(request, 'blog/post_detail.htm', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('posteos', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_new.htm', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(RegistroRescatados, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.htm', {'form': form})


def posteos(request):
        posts = RegistroRescatados.objects.filter(Estado='D')
        return render(request, 'blog/posteos.htm', {'posts': posts})

def formulario(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('formulario', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/formulario.htm', {'form': form})