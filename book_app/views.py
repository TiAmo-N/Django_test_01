from django.shortcuts import render,HttpResponse

def index(request):
    '''
    访问首页
    :param request:
    :return:
    '''
    return HttpResponse('index')

def reg(request):
    '''
    增加一个注册
    :param request:
    :return:
    '''
    return HttpResponse('reg')

