from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    my_title = "Home"
    context = {"title": my_title, "my_list": [1, 2, 3, 4]}
    return render(request, "home.html", context)
