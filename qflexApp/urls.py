from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('user/sign-up/', views.signUpPage, name='signUpPage'),
    path('user/login/', views.loginPage, name='loginPage'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
    path('movies/all/', views.allMoviesPage, name='allMoviesPage'),
    path('movies/all/<slug:slug>/', views.allMoviesPage, name='filterMoviesPage'),
    path('movies/top/', views.topMoviesPage, name='topMoviesPage'),
    path('movie/detail/<int:pk>', views.movieDetailPage, name='movieDetailPage'),
]