from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from . import models
from . import forms


def post_list(request):
    """投稿一覧ページ"""
    posts = models.Post.objects.filter(
        published_date__lte=timezone.now(),
    )
    posts = posts.order_by('-published_date')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })


def post_detail(request, pk):
    """投稿ページ"""
    post = get_object_or_404(models.Post, pk=pk)
    comment_list = post.comment_set.all()

    if request.method == 'POST':
        form = forms.CommentForm(request.POST or None)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': forms.CommentForm,
        'comment_list': comment_list,
    })


def comment_delete(request, pk, comment_pk):
    """Comment delete"""
    comment = get_object_or_404(models.Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('post_detail', pk=pk)
