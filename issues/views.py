from django.shortcuts import render

# Create your views here.
def issues(request):
    return render(request, "issues.html")