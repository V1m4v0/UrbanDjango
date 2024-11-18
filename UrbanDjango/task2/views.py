from django.shortcuts import render
from django.views.generic import TemplateView

def func_template(request):
    return render(request, 'second_template/func_template.html')

class class_template(TemplateView):
    template_name = 'second_template/class_template.html'
