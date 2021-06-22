from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.
from django.views.generic import TemplateView


class home(TemplateView):
    template_name = 'home.html'


# class add(TemplateView):
#     template_name = 'add.html'
#
#
# class display(TemplateView):
#     template_name = 'display.html'


def add(request):
    if request.method == "POST":
        form = bform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = bform()
        return render(request, 'add.html', {'form': form})


# def display(request):
#     data = blog.objects.all()
#     return render(request, 'display.html', {'data': data})


# class dmeo(TemplateView):
#     template_name = 'dmeo.html'


def test(request):
    result = request.POST['selection']
    print(result)

    if request.method == "POST":
        # form = chform(request.POST)
        # print(form)
        # if form.is_valid():
        data = blog.objects.get(name=result)
        return render(request, 'test.html', {'data': data})


def ch(request):
    data = blog.objects.all()
    print(data)

    if request.method == "POST":
        result = request.POST['selection']
        data1 = blog.objects.get(id=result)

        dict = {
            'data': data,
            'data1': data1
        }
        return render(request, 'dmeo.html', dict)
    return render(request, 'dmeo.html', {'data': data})
