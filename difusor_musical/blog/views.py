from django.shortcuts import render

posts = [
    {
     'author': 'vobh',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'data_posted': 'Junho 06, 2022'
    },
    {
     'author': 'Jane doe',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'data_posted': 'Junho 07, 2022'
    }
]

def home_02(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home_02.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})