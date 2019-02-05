from django.contrib import admin
from .models import Person, Documents


# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('doc', 'first_name', 'last_name')
        }),

        ('Dados complementares', {
            'classes': ('collapse', ),
            'fields': ('age', 'salary', 'photo')
        })
    )
    list_filter = ('age', 'salary')

    # fields = ('doc', ('first_name', 'last_name'), ('age', 'salary'),
    # 'photo', )
    # exclude = ('bio', )
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary',
                    'tem_foto')
    search_fields = ('id', 'first_name',)
    autocomplete_fields = ['doc', ]

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = 'Possui Foto'


class DocumentsAdmin(admin.ModelAdmin):
    search_fields = ['num_doc', ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Documents, DocumentsAdmin)










