from django.shortcuts import render

from app.models import Quote

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', context={'quotes': quotes})

def create(request):
    if request.method == 'POST':
        quote = request.POST.get('quote')
        author = request.POST.get('author')
        new_quote = Quote(quote=quote, author=author)
        new_quote.save()
    return render(request, 'create_quote.html')