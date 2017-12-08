from django.db import models


class AbstractDummmy(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        abstract = True


class OfficeSetup(AbstractDummmy):
    pass


class ItemGroup(AbstractDummmy):
    pass


class Item(AbstractDummmy):
    pass


class OpeningStock(models.Model):
    office = models.ForeignKey(OfficeSetup, blank=True, null=True, on_delete=models.CASCADE)
    miti = models.DateField(null=True)
    item_group = models.ForeignKey(ItemGroup, blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    value = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    specification = models.CharField(blank=True, null=True, max_length=600)
