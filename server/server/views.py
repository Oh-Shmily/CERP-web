'''
Description: 
Author: zhouchen
Date: 2024-11-19 19:46:52
LastEditTime: 2024-11-19 19:47:15
LastEditors: zhouchen
'''
from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")