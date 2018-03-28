from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Category,Page
from .forms import CategoryForm,PageForm,UserForm,UserProfileForm

def index(request):
    category_list=Category.objects.order_by('-likes')[:5]
    page_list=Page.objects.order_by('-views')[:5]
    return render(request,'rango/index.html',context={'categories':category_list,
                                                      'pages':page_list })

def show_category(request,category_name_slug):
    context={}
    try:
        category=Category.objects.get(slug=category_name_slug)
        pages=Page.objects.filter(category=category)
        context['pages']=pages
        context['category']=category
    except Category.DoesNotExist:
        context['pages']=None
        context['category']=None
    return render(request,'rango/category.html',context=context)

def add_category(request):
    form=CategoryForm()
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request,'rango/add_category.html',context={'form':form})

def add_page(request,category_name_slug):
    try:
        category=Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category=None
    form=PageForm()
    if request.method=='POST':
        form=PageForm(request.POST)
        if form.is_valid():
            if category:
                page=form.save(commit=False)
                page.category=page
                page.views=0
                page.save()
                return show_category(request,category_name_slug)
        else:
            print(form.errors)
    return render(request,'rango/add_page.html',context={'form':form,'category':category})

def register(request):
    registered=False
    if request.method == 'POST':
        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,'rango/register.html',{'user_form':user_form,
                                                 'profile_form':profile_form,
                                                 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('rango:index'))
            else:
                return HttpResponse('账号未激活,禁止登入')
        else:
            print('登入出错:{0},{1}'.format(username,password))
            return HttpResponse('用户名或密码错误')
    else:
        return render(request,'rango/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('rango:index'))
