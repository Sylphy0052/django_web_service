from django.urls import path

from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.home, name='index'),
    path('<int:pk>/', views.bbs_threads, name='bbs_threads'),
    path('<int:pk>/new/', views.new_thread, name='new_thread'),
]
