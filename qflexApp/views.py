from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q

def homePage(request):
    return render(request, "primaryFrontend/index.html")

def allMoviesPage(request, slug=None):
    genre = None
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        movies = Movie.objects.filter(Q(movieName__icontains=searchData) | Q(description__icontains=searchData))
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        movies = movies.filter(genre=genre)
    return render(request, "primaryFrontend/all-movies.html", {
        'movies': movies,
        'genres': genres,
        'genre': genre
    })

def topMoviesPage(request):
    movie = Movie.objects.all()[:1]
    movies = Movie.objects.all()[:10]
    return render(request, "primaryFrontend/top-movies.html", {
        'movie': movie,
        'movies': movies
    })

def movieDetailPage(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    return render(request, "primaryFrontend/movie-detail.html", {
        'movie': movie
    })

def signUpPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
    else:
        form = NewUserForm()

    return render(request, "user/sign-up.html", {
        'form': form
    })

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("allMoviesPage")
    else:
        form = AuthenticationForm()

    return render(request, "user/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect("homePage")