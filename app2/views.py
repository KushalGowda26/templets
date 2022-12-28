from django.shortcuts import render

# Create your views here.
def second(request):
    return render(request, 'second.html')

def second_child(request):
    return render(request, 'second_child.html')