from django.forms import ModelForm

from genres.models import Genre


class GenreCreateForm(ModelForm):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
            'parent',
        ]

