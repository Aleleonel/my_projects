from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Person
from produtos.models import Product
from vendas.models import Sales
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import View
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views clientes here.


@login_required
def persons_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    if nome or sobrenome:
        persons = Person.objects.filter(first_name__icontains=nome)|Person.objects.filter(last_name__icontains=sobrenome)
    else:
        persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Cliente não autorizado')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonListView(LoginRequiredMixin, ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Voce ja acessou hoje'

        return context

class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Sales.objects.filter(person_sales_id=self.object.id)

        return context


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    success_url = '/clientes/person_list/'


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = (
        ('clientes.deletar_clientes', )
    )

    model = Person
    success_url = reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['banana', 'maca', 'limao', 'laranja',
                    'pera', 'melancia']
        list_produtos = []

        for produto in produtos:
            p = Product(description=produto, price=10)
            list_produtos.append(p)
        Product.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou intens inseridos com sucesso!')



