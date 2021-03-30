from collections import namedtuple
from django.urls import path
from rest_framework import routers
from api import views



urlpatterns = []


urlpatterns +=[
    # path('category-create/', views.BookCategoryCreate.as_view()),
    # path('category-list-create/', views.BookCategoryListCreate.as_view()),
    path('category-retrieve/<int:pk>/', views.BookCategoryRetrieveView.as_view()),
    path('category-update/<int:pk>/', views.BookCategoryUpdateView.as_view()),
    path('category-retrieve-update/<int:pk>/', views.BookCategoryRetrieveView.as_view()),
    path('category-destroy/<int:pk>/', views.BookCategoryDestroyView.as_view()),





   
]