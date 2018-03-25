from django.shortcuts import render
from .models import Category,Page

def index(request):
    category_list=Category.objects.order_by('-likes')[:5]
    page_list=Page.objects.order_by('views')[:5]
    return render(request,'rango/index.html',context={'category_list':category_list,
                                                      'page_list':page_list
                                                      })

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
