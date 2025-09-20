from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
 #   return HttpResponse("Hello from My App!")
    return render(request, 'rentalsextenalcss/home.html')

def review(request):
    return render(request, 'rentalsextenalcss/review.html')