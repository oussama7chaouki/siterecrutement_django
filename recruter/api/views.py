from django.shortcuts import render
from django.http import HttpResponse
import datetime


def test(request):
 return render(request, 'recruter/test.html')