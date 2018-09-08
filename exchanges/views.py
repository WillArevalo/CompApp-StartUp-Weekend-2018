from django.shortcuts import render

# Create your views here.

def list_exchanges(request):
	return render(request, 'feed.html')