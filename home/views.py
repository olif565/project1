from django.shortcuts import render, redirect, get_object_or_404
from .models import Data
from .forms import DataForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Data.objects.all()


class DataDetailView(DetailView):
    model = Data
    template_name = 'data-detail.html'


def create(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home_view')
    form = DataForm()

    return render(request, 'create.html', {'form': form})


def edit(request, pk, template_name='edit.html'):
    contact = get_object_or_404(Data, pk=pk)
    form = DataForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home:home_view')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(Data, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home:home_view')
    return render(request, template_name, {'object': contact})
