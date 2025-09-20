from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
 #   return HttpResponse("Hello from My App!")
    active_class = "index"
    harmful_variable = "<script>alert('hello')</script>"
    context = {
        'active_class': active_class,
        'harmful_variable':harmful_variable,
    }
    return render(request, 'rentalsmodel/home.html', context)

def review(request):
    active_class = "review"
    harmful_variable = "<script>alert('hello')</script>"
    context = {
        'active_class': active_class,
        'harmful_variable':harmful_variable,
    }
    return render(request, 'rentalsmodel/review.html', context)