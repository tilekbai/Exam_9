from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

from .models import *
from .forms import *
# Create your views here.


class IndexView(ListView):
    model = Photo
    template_name = "photo/index.html"
    context_object_name = 'photos'
    ordering = ('-date')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(author__icontains=self.search_data) |
                Q(content__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class PhotoView(DetailView):
    model = Photo
    template_name = 'photo/view.html'


class CreatePhotoView(CreateView):
    template_name = 'photo/create.html'
    form_class = PhotoForm
    model = Photo
    success_url = reverse_lazy('gallery:index')


class PhotoUpdateView(UpdateView):
    form_class = PhotoForm
    model = Photo
    template_name = 'photo/update.html'
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('gallery:view-photo', kwargs={'pk': self.kwargs.get('pk')})


