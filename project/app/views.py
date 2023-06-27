from django.shortcuts import render

from app.models import Quote

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', context={'quotes': quotes})