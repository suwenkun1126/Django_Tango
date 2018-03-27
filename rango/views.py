from django.shortcuts import render
from .models import Category,Page
from .forms import CategoryForm,PageForm

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