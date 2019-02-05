from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from vendas.models import Sales


# Create your views Vendas here.


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso Negado, vocẽ não tem permissão para visualizar')
        
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['media'] = Sales.objects.media()
        data['media_desc'] = Sales.objects.media_desc
        data['min'] = Sales.objects.min()
        data['max'] = Sales.objects.max()
        data['n_ped'] = Sales.objects.n_ped()
        data['n_ped_nfe'] = Sales.objects.n_ped_nfe()

        return render(request, 'vendas/dashboard.html', data)


