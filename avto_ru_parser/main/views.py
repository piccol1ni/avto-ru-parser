from django.shortcuts import render
import xml.etree.ElementTree as ET
 

def index(request):
    tree = ET.parse('./income_info/cars.xml')
    root = tree.getroot()
    print(1)
    for elem in root.findall('folder'):
        print(elem.attrib)

    context = {}
    return render(request, 'main/index.html', context)
