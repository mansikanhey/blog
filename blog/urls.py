from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('/about/', views.AboutPageView.as_view(), name='about'),
    path('/contact/', views.ContactPageView.as_view(), name='contact'),
    path('<slug:slug>/', views.detail, name='detail'),
    

    

]