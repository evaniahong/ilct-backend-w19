from django.urls import path

from . import views

urlpatterns = [
    # ex: /business/
    path('', views.index, name='index'),
    # ex: /business/5/
    path('<int:business_id>/', views.detail, name='detail'),
]