from django.shortcuts import render

def platform(request):
    return render(request, 'fourth_task/platform.html')

def shop(request):
    games = ['Atomic heart', 'Cuberpunk 2077', 'S.T.A.L.K.E.R. COP']
    context = {
        'games': games,
    }
    return render(request, 'fourth_task/shop.html', context)

def basket(request):
    return render(request, 'fourth_task/basket.html')

def menu(request):
    return render(request, 'fourth_task/menu.html')