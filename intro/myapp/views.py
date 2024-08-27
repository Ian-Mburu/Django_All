from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    blogs = [
        {
            'title': 'Software Development',
            'content': 'This is a blog about software development',
            'date': '2022-01-01'
            
        },
        {
            'title': 'Software Development',
            'content': 'This is a blog about software development',
            'date': '2022-01-01'
            
        },
        {
            'title': 'Software Development',
            'content': 'This is a blog about software development',
            'date': '2022-01-01'
            
        }
    ]

    context = {'blogs': blogs}
    return render(request, 'index.html', context)