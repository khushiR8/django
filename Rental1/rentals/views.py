from django.shortcuts import render

# Create your views here.
def index(request):
 #   return HttpResponse("Hello from My App!")
    return render(request, 'rentals/home.html')

def review(request):
    return render(request, 'rentals/review.html')