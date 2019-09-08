from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
]
