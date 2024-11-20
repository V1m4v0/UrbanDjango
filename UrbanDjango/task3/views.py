from django.shortcuts import render

def platform(request):
    return render(request, 'third_task/platform.html')

def shop(request):
    button_back = 'Вернуться обратно'
    context = {
        'button_back': button_back,
    }
    return render(request, 'third_task/Magazine.html', context)

def basket(request):
    button_back = 'Вернуться обратно'
    context = {
        'button_back': button_back,
    }
    return render(request, 'third_task/basket.html', context)