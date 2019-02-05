from django.db import models
from django.db.models import Sum, F, FloatField, Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Product
from .managers import SalesManagers

# Create your models vendas here.


class Sales(models.Model):
    num_sales = models.CharField(max_length=7)
    value_sales = models.DecimalField(max_digits=5,decimal_places=2,
                                      null=True, blank=True)
    desc = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    taxes = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    person_sales = models.ForeignKey(Person, null=True, blank=True,
                                     on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)
    objects = SalesManagers()

    class Meta:
        permissions = (
            ('setar_nfe', 'Usuário pode alterar parametro NF-e'),
            ('ver_dashboard', 'Usuário pode visualizar Dashborad'),
            ('permissao3', 'Permissao3'),
        )

    def calcular_total(self):
        tot = 0.0
        desconto = 0.0

        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum((F('quantity') * F('product__price')) - F('desc'),
                        output_field=FloatField()))['tot_ped'] or 0

        desconto = float(tot) * (float(self.desc)/100)
        impostos = float(tot) * (float(self.taxes)/100)

        tot -= desconto
        tot += impostos

        tot_total = tot

        self.value_sales = tot_total
        Sales.objects.filter(id=self.id).update(value_sales=tot_total)

    def __str__(self):
        return self.num_sales


class ItemDoPedido(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    desc = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.sale.num_sales + ' - ' + self.product.description


@receiver(post_save, sender=ItemDoPedido)
def update_sales_total(sender, instance, **kwargs):
    instance.sale.calcular_total()


@receiver(post_save, sender=Sales)
def update_sales_total2(sender, instance, **kwargs):
    instance.calcular_total()
