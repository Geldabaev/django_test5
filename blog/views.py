from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return render(request, "blog/index.html", {})


def categ(request, catid):
    if request.GET:
        print(request.GET)
    if int(catid) == 100:
        raise Http404
    if int(catid) == 200:
        return redirect('home')
    if int(catid) == 300:
        return redirect('/', permanent=True)
    return HttpResponse(f"<h1>page{catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страницы нет браток</h1>")
