# -*- coding:utf-8 -*-
# @author:sumin
from django.shortcuts import render, redirect
from .models import Con
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage

# Create your views here.
def index(request):
    try:
        item_list = Con.objects.all().order_by('-pubdate')
        pagobj = Paginator(item_list, 5)
        try:
            page = int(request.GET.get('page', 1))
            item_list = pagobj.page(page)
        except (PageNotAnInteger, InvalidPage, EmptyPage):
            item_list = pagobj.page(1)
    except Exception as e:
        print(e)
    return render(request, 'index.html', locals())

def add(request):
    try:
        content_list = request.GET.get('add_content', None)
        if len(content_list) > 0:
            obj = Con.objects.create(content_list=content_list)
            if obj:
                return redirect('/index/')
    except Exception as e:
        print(e)
    return render(request, 'error1.html', {'error1':u'保存出错,事项添加失败'})

def delete(request):
    try:
        item_id = request.GET.get('item_id',None)
        if len(item_id) > 0:
            obj =  Con.objects.get(pk = item_id)
            obj.delete()
        return redirect('/index/')
    except Exception as e:
        print(e)
    return render(request, 'error1.html', {'error1': u'事项删除失败'})

def edit(request):
    try:
        item_id = request.GET.get('item_id',None)
        content = request.GET.get('item', None)
        if len(item_id) > 0 and len(content) > 0:
            obj =  Con.objects.get(pk = item_id)
            obj.content_list = content
            obj.save()
        return redirect('/index/')
    except Exception as e:
        print(e)
    return render(request, 'error1.html', {'error1': u'事项编辑失败'})

def flag(request):
    try:
        item_id = request.GET.get('item_id',None)
        if len(item_id) > 0 :
            obj =  Con.objects.get(pk = item_id)
            if obj.flag == True:
                obj.flag = False
            else:
                obj.flag = True
            obj.save()
        return redirect('/index/')
    except Exception as e:
        print(e)
    return render(request, 'error1.html', {'error1': u'事项状态修改失败'})


