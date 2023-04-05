from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.AutoLoginView.as_view(), name='login'),
]
