from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from myBlog.form import CommentForm, UserForm
from myBlog.models import Blog, Comment
from django.contrib.auth.models import User


def get_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    blogs = Blog.objects.all().order_by('-pub')
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    if not request.user.is_authenticated:
        return redirect('login')
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'GET':  # 请求方法为get
        form = CommentForm()
    else:  # 请求方法为post
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    content = {
        'blog': blog,
        'form': form,
        'comments': blog.comment_set.all().order_by('-pub'),
    }
    return render(request, 'detail.html', content)


# 主页
def index(request):
    return render(request, 'index.html')


# 注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            addregist = User.objects.create_user(username=username, password=password)
            if addregist == False:  # 注册失败
                return render(request, 'share1.html', {'addregist': addregist, 'username': username})
            else:  # 注册成功
                # return HTTPresponse('ok')
                return render(request, 'share1.html', {'addregist': addregist})
    else:
        # get请求
        uf = UserForm()
    return render(request, 'regist.html', {'uf': uf})


# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        au = auth.authenticate(username=username, password=password)  # 用户认证
        if au is not None:  # 如果数据库里有记录（即与数据库里的数据相匹配或对应）
            auth.login(request, au)  # 登录成功
            return redirect('get_blog')  # 跳转
        else:  # 数据库没有对应数据
            uf = UserForm()
            return render(request, 'regist.html', {'login_error': '用户名或密码错误','uf':uf})
    return render(request, 'login.html')


# 登出
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
