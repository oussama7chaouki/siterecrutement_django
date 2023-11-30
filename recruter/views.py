from django.shortcuts import render
from django.shortcuts import render, redirect

from django.http import HttpResponse
import datetime


def test(request):
 return render(request, 'recruter/test.html')

def offer(request):
 offers = [
    {"id_job": 1, "job_title": "Software Engineer", "domain": "Information Technology", "date": "2023-11-28"},
    {"id_job": 2, "job_title": "Financial Analyst", "domain": "Finance", "date": "2023-11-25"},
    {"id_job": 3, "job_title": "Marketing Manager", "domain": "Marketing", "date": "2023-11-20"},
    ]
 context = {'offers': offers}
 return render(request, 'recruter/jobs.html',context)
def jobcans(request):
 jobcan=[{
    "date": "2023-11-29",
    "title": "Software Engineer",
    "domain": "Information Technology",
    "count": 10,
    "id":1
  },
  {
    "date": "2023-11-30",
    "title": "Data Analyst",
    "domain": "Analytics",
    "count": 5,
        "id":2

  }]
 context = {'jobcans': jobcan}
 return render(request, 'recruter/jobcans.html',context)
def jobcan(request,pk):
 
 return render(request, 'recruter/jobcan.html')