from django.shortcuts import render, get_object_or_404, redirect

from Gender.forms import GenderForm
from Movie.models import Movie
from Serie.models import Serie
from .models import Gender

# Create your views here.
def gender_list(request, id):
    movies = Movie.objects.filter(gender = id)
    series = Serie.objects.filter(gender = id)
    genders = Gender.objects.all()
    context = {
        'movies': movies,
        'series': series,
        'genders': genders
    }
    return render(request, 'gender/index.html', context)

def gender_detail(request, id):
    gender_detail_by_id = get_object_or_404(Gender, pk=id)
    return render(request, 'gender/show.html', {'gender_detail_by_id': gender_detail_by_id})

def gender_add(request):
    if request.method == 'POST':
        form = GenderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gender_list')
    else:
        form = GenderForm()
    return render(request, 'gender/create.html', {'form': form})

def gender_edit(request, id):
    gender = get_object_or_404(Gender, pk=id)
    if request.method == 'POST':
        form = GenderForm(request.POST, request.FILES, instance=gender)
        if form.is_valid():
            form.save()
            return redirect('gender_list')
    else:
        form = GenderForm(instance=gender)
    return render(request, 'gender/update.html', {'form': form})

def gender_delete(request, id):
    gender_delete = get_object_or_404(Gender, pk=id)
    if request.method == 'POST':
        gender_delete.delete()
        return redirect('gender_list')
    return render(request, 'gender/update.html', {'gender_delete': gender_delete})