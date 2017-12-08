from django.shortcuts import render
from django.views.generic import CreateView

from openingstocks.forms import OpeningStockForm
from openingstocks.models import OpeningStock


class OpeningStockCreateView(CreateView):
    model = OpeningStock
    form_class = OpeningStockForm
    template_name = './openingstock_form.html'
