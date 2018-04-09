from django.test import TestCase

from genres.models import Genre


def fill_database():
    """
    Fill the database follow the question
    https://stackoverflow.com/questions/47644824/child-node-is-treated-as-grand-child-node-when-trying-to-structure
    """

    bedroom = Genre.objects.create(name='Bedroom Items')
    almirah = Genre.objects.create(name='Almirah', parent=bedroom)
    two_pcs_almirah = Genre.objects.create(name='2 pieces almirah', parent=almirah)
    three_pcs_almirah = Genre.objects.create(name='3 pieces almirah', parent=almirah)

    bed = Genre.objects.create(name='Bed', parent=bedroom)
    double_low_bed = Genre.objects.create(name='Double size low bed', parent=bed)
    queen_low_bed = Genre.objects.create(name='Queen size low bed', parent=bed)
    single_low_bed = Genre.objects.create(name='Single size low bed', parent=bed)

    dressing_tbl = Genre.objects.create(name='Dressing Table', parent=bedroom)

    kitchen_ware = Genre.objects.create(name='Kitchen Wares')
    dinningset = Genre.objects.create(name='Dinning Set', parent=kitchen_ware)
    kitchen_rack = Genre.objects.create(name='Kitchen Rack', parent=kitchen_ware)
    kitchen_setup = Genre.objects.create(name='Kitchen Setup(Modular Kitchen)', parent=kitchen_ware)

    mod_kitchen = Genre.objects.create(name='Moduler Kitchen')

