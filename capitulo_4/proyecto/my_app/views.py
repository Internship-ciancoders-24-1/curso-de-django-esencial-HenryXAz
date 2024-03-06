"""Proyecto views"""
from django.http import HttpResponse, JsonResponse
from datetime import  datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %d th, %Y - %H:%M hrs')
    return HttpResponse("Oh, hi! Current server time is {now}".format(now=str(now)))

def sort_numbers(request):
    # import pdb; pdb.set_trace()
    numbers_list = request.GET['numbers'].split(',')
    numbers = [int(number) for number in numbers_list ]
    numbers.sort()
    
    data = {}
    data['sorted_numbers'] = numbers
    data['message'] = 'success'
    return JsonResponse(data)


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'hello, {}! welcome to my app'.format(name)

    return HttpResponse(message)