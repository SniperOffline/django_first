from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from blog.models import Category, Blog, Comment


# Create your views here.

def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    context = {
        'blogs' : blogs
    }

    return render(request, 'blog/index.html', context)
def registration(request):
    return render(request, 'blog/registration.html')
def signUp(request):
    if request.POST:
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password != confirm:
            messages.error(request, "Parollar bir xil emas")
            return redirect('reg')
        
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.second_name = second_name
        user.save()
        messages.success(request, 'Muvaffaqqiyatli ro`yxatdan o`tdingiz')
        return redirect('signIn')
    else:
        return redirect('reg')

def signIn(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Siz akkauntingizga kirdingiz')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Login yoki parol xato')
            return redirect('logIn')
    else:
        return redirect('logIn')

def logIn(request):
    return render(request, 'blog/signIn.html')

def logout_url(request):
    logout(request)
    messages.success(request, 'Siz muvaffaqqiyatli akkauntdan chiqdingiz')
    return redirect(signIn)


@login_required
def create_blog_form(request):
    context = {
        'categories' : Category.objects.all()
    }
    return render(request, 'blog/create-blog-form.html', context)

@login_required
def create_blog(request): 
    if request.POST:
        title       = request.POST.get('title')
        poster      = request.FILES.get('poster')
        content     = request.POST.get('content')
        category_id = request.POST.get('category')
        author      = request.user

        category = Category.objects.get(pk = category_id)

        Blog.objects.create(
            title = title,
            poster = poster,
            content = content,
            category = category,
            author = author
        )

        messages.success(request, 'Blog muvaffaqqiyatli yaratildi')
        return redirect('index')
    
@login_required
def delete_blog(request, blog_id):
    if request.POST:
        blog = Blog.objects.get(pk=blog_id)
        if request.user == blog.author:
            blog.delete()
            messages.success(request, 'Blog o`chirildi')
            return redirect('index')
        else:
            messages.error(request, 'O`zingnikini o`chir boshqanikiga tegma!!!')
            return redirect('index')
    else:
        blog = Blog.objects.get(pk = blog_id)
        context = {
            'blog': blog
        }
        return render(request, 'blog/blog-delete-confirm.html', context)

@login_required
def delete_comment(request, comment_id):
    if request.POST:
        comment = Comment.objects.get(pk=comment_id)
        if request.user==comment.author:
            comment.delete()
            messages.success(request, 'Commentariya o`chirildi')
            return redirect('index')
    else:
        messages.error(request, 'Comment o`chirilmadi')
        return render(request, 'blog/index.html')


@login_required
def blog_model(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    context = {
        'blog' : blog
    }
    return render(request, 'blog/blog-detail.html', context)

@login_required
def add_comment(request, blog_id):
    if request.POST:
        content = request.POST.get('comment')
        author = request.user
        blog = Blog.objects.get(id = blog_id)
        Comment.objects.create(content = content, author=author, blog= blog)
        
        messages.success(request, 'Comment muvaffaqqiyatli yaratildi')
        return redirect('blog-detail', blog_id = blog_id)