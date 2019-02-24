from django.http.response import HttpResponse
from django.shortcuts import render


# 测试视图
def test(request):
    a=5
    return HttpResponse("测试视图")
