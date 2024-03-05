from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


posts = [
    {
        'name' : 'Mont Blanc',
        'user' : 'Yessica Cortés',
        'timestamp' : datetime.now().strftime('%b %d th, %Y - %H:%M hrs'),
        'pictures': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name' : 'Via Lactea',
        'user' : 'C. Vader',
        'timestamp' : datetime.now().strftime('%b %d th, %Y - %H:%M hrs'),
        'pictures': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name' : 'Nuevo auditorio',
        'user' : 'Thespianartis',
        'timestamp' : datetime.now().strftime('%b %d th, %Y - %H:%M hrs'),
        'pictures': 'https://picsum.photos/200/200/?image=1076',
    }
]


# Create your views here.

def list_posts(request):
    return render(request, 'feed.html', {'posts' : posts})

# def list_posts(request):
#     content = []

#     for post in posts:
#         content.append("""
#             <p><strong>{name}</strong></p>
#             <p><small>{user} - <i>{timestamp}</i></small></p>
#             <figure><img src={pictures} /></figure> 
#                        """.format(**post))
#     return HttpResponse('<br>'.join(content))