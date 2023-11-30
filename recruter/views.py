from django.shortcuts import render, redirect

from .models import Job,Candidature,User


def test(request):
 return render(request, 'recruter/test.html')

def offer(request):
 offers=Job.objects.all()
#  offers = [
#     {"id": 1, "title": "Software Engineer", "domain": "Information Technology", "date": "2023-11-28"},
#     {"id": 2, "title": "Financial Analyst", "domain": "Finance", "date": "2023-11-25"},
#     {"id": 3, "title": "Marketing Manscorer", "domain": "Marketing", "date": "2023-11-20"},
#     ]

 context = {'offers': offers}
 return render(request, 'recruter/jobs.html',context)
def jobcans(request):
 jobcans=Job.objects.all()
#  jobcan=[{
#     "date": "2023-11-29",
#     "title": "Software Engineer",
#     "domain": "Information Technology",
#     "count": 10,
#     "id":1
#   },
#   {
#     "date": "2023-11-30",
#     "title": "Data Analyst",
#     "domain": "Analytics",
#     "count": 5,
#         "id":2

#   }]
 context = {'jobcans': jobcan}
 return render(request, 'recruter/jobcans.html',context)
def jobcan(request,pk):
   datas = [
      {'name': 'Alice', 'score': 25, 'email': 'alice@example.com'},
      {'name': 'Bob', 'score': 30, 'email': 'bob@example.com'},
      {'name': 'Charlie', 'score': 22, 'email': 'charlie@example.com'},
   ]
   context = {'datas': datas}
   return render(request, 'recruter/jobcan.html',context)