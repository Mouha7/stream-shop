from django.shortcuts import get_object_or_404, redirect, render
from Gender.models import Gender
from Serie.forms import SerieForm
from .models import Serie

# Create your views here.
def serie_list(request):
    series = Serie.objects.all()
    genders = Gender.objects.all()
    return render(request, 'serie/index.html', {'series': series, 'genders': genders})

def serie_detail(request, id):
    serie_detail_by_id = get_object_or_404(Serie, pk=id)
    genders = Gender.objects.all()
    return render(request, 'serie/show.html', {'serie_detail_by_id': serie_detail_by_id, 'genders': genders})

def serie_add(request):
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
    else:
        form = SerieForm()
    return render(request, 'serie/create.html', {'form': form})

def serie_edit(request, id):
    serie = get_object_or_404(Serie, pk=id)
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
    else:
        form = SerieForm(instance=serie)
    return render(request, 'serie/update.html', {'form': form, 'serie': serie})

def serie_delete(request, id):
    serie_delete = get_object_or_404(Serie, pk=id)
    if request.method == 'POST':
        serie_delete.delete()
        return redirect('serie_list')
    return render(request, 'serie/update.html', {'serie_delete': serie_delete})