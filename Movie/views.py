from django.shortcuts import get_object_or_404, redirect, render

from Gender.models import Gender
from Movie.forms import MovieForm
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    genders = Gender.objects.all()
    return render(request, 'movie/index.html', {'movies': movies, 'genders': genders})

def movie_detail(request, id):
    movie_detail_by_id = get_object_or_404(Movie, pk=id)
    genders = Gender.objects.all()
    return render(request, 'movie/show.html', {'movie_detail_by_id': movie_detail_by_id, 'genders': genders})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/create.html', {'form': form})

def movie_edit(request, id):
    movie = get_object_or_404(request, pk=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/update.html', {'form': form})

def movie_delete(request, id):
    movie_delete = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        movie_delete.delete()
        return redirect('movie_list')
    return render(request, 'movie/update.html', {'movie_delete': movie_delete})