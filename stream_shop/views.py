from django.shortcuts import render
from Gender.models import Gender
from Movie.models import Movie
from Serie.models import Serie

def home(request):
    latest_movies = Movie.objects.order_by('-release_date')[:5]
    latest_series = Serie.objects.order_by('-release_date')[:5]
    genders = Gender.objects.all()
    context = {
        'latest_movies': latest_movies,
        'latest_series': latest_series,
        'genders': genders
    }
    return render(request, 'home.html', context)