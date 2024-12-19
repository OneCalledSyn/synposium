from django.shortcuts import render

# Create your views here.

# render() looks for HTML templates inside templates/ directory
def home(request):
    return render(request, "pages/home.html", {})