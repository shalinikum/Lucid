from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/fetch_user_task/', views.fetch_user_task, name='tasks'),
    path('<int:attribute_id>/fetch_words/', views.fetch_words, name='words'),

]