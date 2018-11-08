from django.urls import path

from . import views

app_name = 'bbs'
urlpatterns = [
    # Top Page
    path('', views.IndexView.as_view(), name='index'),
    # Thread List
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Thread Detail
    # path('<int:pk>/')
]
