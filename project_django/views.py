# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def home_view(request):
    return render(request, 'home.html')


class MyView(View):
    def get(self, request):
        # <view logic>
        # return HttpResponse("Hello from MyView!")
        return render(request, 'home.html')