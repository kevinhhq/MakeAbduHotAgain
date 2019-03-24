from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import  food_table
from .forms import UserForm
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html",{})

def search(request):
    query=request.GET.get('q')
    error_msg = ''
    if not query:
        error_msg = 'enter key word'
        return render(request, 'results.html', {'error_msg': error_msg})
    results = food_table.objects.filter(Q(Name__icontains=query))
    return render(request, "results.html" ,{'error_msg': error_msg, 'results': results})

def user_create_view(request, *args, **kwargs):
    form=UserForm(request.POST)
    if form.is_valid():
        form.save()
        form=UserForm

    context={
        'form':form
    }
    return render(request, "user_create.html",context)

def update_view(request, id=id):
    obj = food_table.objects.get(id=id)
    form = UserForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "user_create.html", context)

def detail_view(request,id):
    try:
        obj=food_table.objects.get(id=id)
    except food_table.DoesNotExist:
        raise Http404
    detail={
        'object':obj
    }
    return render(request, "detail.html",detail)

def delete_view(request,id):
    obj=food_table.objects.get(id=id)
    obj.delete()
    queryset = food_table.objects.all()
    context = {
        "User_list": queryset
    }
    return render(request, 'list.html',context)

def list_view(request):
    queryset= food_table.objects.all()
    context={
        "User_list":queryset
    }
    return render(request, "list.html", context)