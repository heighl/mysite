from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from MyBlog.forms import CommentForm
from MyBlog.models import BlogPost, comment


def get_blog(request):
    blogs = BlogPost.objects.all().order_by('-pub')
    return render(request, 'blog_list.html', {'blogs': blogs})


def get_details(request, blog_id):
    # 检查异常
    try:
        blog = BlogPost.objects.get(id=blog_id)  # 获取固定的blog_id的对象；
    except BlogPost.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:  # 请求方法为Post
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-pub'),
        'form': form
    }  # 返回3个参数
    return render(request, 'blog_detail.html', ctx)
