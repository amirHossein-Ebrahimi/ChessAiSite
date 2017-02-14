from django.shortcuts import *


def index(request):
    return render(request, "ChessAiSite_app/index.html")
