from django.shortcuts import get_object_or_404, render

from .models import Category, Comment, Post, User


def main(request):
    return render(request, 'main.html')


def users(request):
    return render(request, 'users.html', {'users': User.objects.all()})


def blogs(request):
    return render(request, 'blogs.html', {'posts': Post.objects.select_related('category')})


def blogdetails(request, post_id):
    post = get_object_or_404(Post.objects.select_related('category'), pk=post_id)
    comments = post.comments.select_related('user')
    return render(request, 'blogdetails.html', {'post': post, 'comments': comments})


def comments(request):
    comment_list = Comment.objects.select_related('post', 'user')
    return render(request, 'comments.html', {'comments': comment_list})


def categories(request):
    return render(request, 'categories.html', {'categories': Category.objects.all()})
