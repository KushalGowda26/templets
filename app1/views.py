from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')

def first_child(request):
    return render(request,'first_child.html')