from django.shortcuts import render

def index(request):
	"""the index page"""
	return render(request, 'learning_logs/index.html')
