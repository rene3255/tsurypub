from django.shortcuts import render

def index(request):
    context = {'greetings': 'Saludos desde la view'}
    return render(request, 'matrix/index.html', context)

