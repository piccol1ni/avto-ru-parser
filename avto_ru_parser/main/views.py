from django.shortcuts import render, redirect
from django.contrib import messages

import xml.etree.ElementTree as ET

from main.models import Mark, Model
 

def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def reload_auto_base(request):
    context = {}
    tree = ET.parse('./income_info/cars.xml')
    root = tree.getroot()
    marks = root.findall('mark')
    if request.method == 'POST':
        Mark.objects.all().delete()
        Model.objects.all().delete()
        for mark in marks:
            
            new_mark = Mark(name=mark.get('name'))
            new_mark.save()
            for i in mark.findall('folder'):
                try:
                    Model.objects.get(name = i.attrib['name'].split(',')[0])
                except Exception:
                    print('Такая модель уже существует')
                    new_model = Model(name = i.attrib['name'].split(',')[0], mark = new_mark)
                    new_model.save()
        messages.success(request, 'База автомобилей успешно обновлена!')
        return redirect('/')
    return redirect('/')

def show_models(request):
    if request.method == 'POST':
        auto_models = Model.objects.filter(mark=Mark.objects.get(name= request.POST['mark']))
        context = {
            'auto_models': auto_models,
        }
    return render(request, 'main/index.html', context)
