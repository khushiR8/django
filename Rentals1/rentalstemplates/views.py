from django.shortcuts import render

# Create your views here.
def index(request):
 #   return HttpResponse("Hello from My App!")
    active_class = "index"
    context = {
        'active_class': active_class,
    }
    return render(request, 'rentalstemplates/home.html', context)

def review(request):
    active_class = "review"
    context = {
        'active_class': active_class,
    }
    return render(request, 'rentalstemplates/review.html', context)