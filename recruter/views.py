from django.shortcuts import render, redirect

from .models import Job,Candidature,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm


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

def loginPage(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('offer')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=email)
        except:
            messages.error(request, 'User does not exist')
            return render(request, 'recruter/login.html', context)

                 # Check if the user's role is not equal to 1
        if user.role != 1:
            messages.error(request, 'You do not have permission to login')
            return render(request, 'recruter/login.html', context)
        
        user = authenticate(request, username=email, password=password,role=1)

        if user is not None:
            login(request, user)
            return redirect('offer')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'recruter/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('offer')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'recruter/login.html', {'form': form})

       
