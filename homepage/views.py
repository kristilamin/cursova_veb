from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Order, Product, Surovuna
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


def homepage(request):
    return render(request, 'homePage.html')


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'userPage.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = context['order'].filter(user_id=self.request.user)
        context['count'] = context['order'].exclude(order_status="Закрито").count()    # кількість замовлень з не закритим статусом
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['order'] = context['order'].filter(product_id__product_name__icontains=search_input)
            context['search_input'] = search_input
        return context



class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        queryset = super().get_queryset().select_related('product_id')
        return get_object_or_404(queryset, id=self.kwargs['pk'])



class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['product_id', 'quantity_of_product']
    # fields = "__all__"
    success_url = reverse_lazy('order')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(CreateOrder, self).form_valid(form)



class DeleteOrder(LoginRequiredMixin, DeleteView):
    model = Order
    context_object_name = 'order'
    template_name = 'order_delete.html'
    success_url = reverse_lazy('order')



# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     fields = "__all__"
#     redirect_authenticated_user = False

#     def get_success_url(self):
#         return reverse_lazy('order')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        if self.request.user.is_superuser:  # перевіряємо, чи користувач має права адміністратора
            return reverse_lazy('admin-page')  # якщо має, то перенаправляємо на сторінку адміністратора
        else:
            return reverse_lazy('order')  # якщо ні, то перенаправляємо на сторінку зі списком замовлень



class СatalogueView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalogue.html'
    context_object_name = 'product'



class AdminPage(LoginRequiredMixin, ListView):
    template_name = 'admin_page.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.all()
        products = Product.objects.all()
        surovunas = Surovuna.objects.all()
        return {'orders': orders, 'products': products, 'surovunas': surovunas}