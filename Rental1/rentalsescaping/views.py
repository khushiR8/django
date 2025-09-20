from django.shortcuts import render

# Create your views here.
def index3(request):
 #   return HttpResponse("Hello from My App!")
    active_class = "index"
    harmful_variable = "<script>alert('hello')</script>"
    #harmful_variable = "<script>window.location= 'http://harmfulsite/mypage'</script>"
    context = {
        'active_class': active_class,
        'harmful_variable':harmful_variable,
    }
    return render(request, 'rentalsescaping/home.html', context)

def review3(request):
    active_class = "review"
    harmful_variable = "<script>alert('hello')</script>"
    context = {
        'active_class': active_class,
        'harmful_variable':harmful_variable,
    }
    return render(request, 'rentalsescaping/review.html', context)