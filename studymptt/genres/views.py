from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from genres.forms import GenreCreateForm
from genres.models import Genre


class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        context['nodes'] = context.get('object_list')
        return super().get_context_data(**context)


class GenreCreateView(CreateView):
    model = Genre
    template_name = 'genre_create.html'
    form_class = GenreCreateForm
    success_url = reverse_lazy('genre:list')


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'

    def get_context_data(self, **kwargs):
        """
        Follow the example https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#detailview
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        return context


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'genre_confirm_delete.html'
    success_url = reverse_lazy('genre:list')
