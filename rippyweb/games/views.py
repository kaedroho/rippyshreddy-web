from django.shortcuts import render


def play(request):
    return render(request, 'games/play.html')
