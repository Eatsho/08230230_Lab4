from django.shortcuts import render

# Home page view
def index(request):
    return render(request, 'tlJourney/tlindex.html')

# About Me page view
def aboutMe(request):
    return render(request, 'tlJourney/aboutMe.html')

