from django.shortcuts import render

def index(request):
    submitted = False
    username = ""
    if request.method == "POST":
        username = request.POST.get("username")
        submitted = True
    return render(request, "renting/index.html", {"submitted": submitted, "username": username})

def about(request):
    return render(request, "renting/about.html")
