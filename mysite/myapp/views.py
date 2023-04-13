from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request,'index.html')

def counter (request):
    text = request.GET['text']
    amount = len(text.split())
    return render (request,'counter.html', {'amount':amount})
