from django.db import models
from django.db.models import Max, Avg, Min, Count


class SalesManagers(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('value_sales'))['value_sales__avg']

    def media_desc(self):
        return self.all().aggregate(Avg('desc'))['desc__avg']

    def min(self):
        return self.all().aggregate(Min('value_sales'))['value_sales__min']

    def max(self):
        return self.all().aggregate(Max('value_sales'))['value_sales__max']

    def n_ped(self):
        return self.all().aggregate(Count('id'))['id__count']

    def n_ped_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']
