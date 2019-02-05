from django.contrib import admin
from .models import Sales
from .models import ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class SalesAdmin(admin.ModelAdmin):
    readonly_fields = ('value_sales',)
    autocomplete_fields = ('person_sales', )
    list_filter = ('person_sales__doc', 'desc')
    list_display = ('id', 'person_sales', 'nfe_emitida', )
    search_fields = ('id', 'person_sales__first_name',
                     'person_sales__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemPedidoInline]

    def total(self, obj):
        return obj.get_total()
    total.short_description = 'Total'


admin.site.register(Sales, SalesAdmin)
admin.site.register(ItemDoPedido)
