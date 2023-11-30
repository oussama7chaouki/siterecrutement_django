from django.urls import path
from . import views

urlpatterns = [

    path('', views.test,name="test"),
    path('offer', views.offer,name="offer"),
    path('jobcans', views.jobcans,name="jobcans"),
    path('jobcan/<str:pk>/', views.jobcan,name="jobcan"),



]
    # path('admin/', views.site.urls),
    # path('joboffer/<str:pk>', views.site.urls,name="joboffer"),
    # path('jobs', views.site.urls,name="jobs"),
    # path('message', views.site.urls,name="message"),