from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import OrderList, OrderDetail, CreateOrder, DeleteOrder, CustomLoginView, СatalogueView, AdminPage
from django.contrib.auth.views import LogoutView
from django.urls import include
from django.contrib import admin


# urlpatterns = [
#     path('', views.homepage, name='homepage'),
# ]

urlpatterns = [
    path('order-create/', CreateOrder.as_view(), name='order-create'),
    path('order/', OrderList.as_view(), name='order'),
    path('', views.homepage, name='homepage'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order-delete/<int:pk>/', DeleteOrder.as_view(), name='order-delete'),
    path('catalogue/', СatalogueView.as_view(), name='catalogue'),

    path('admin-page/', AdminPage.as_view(), name='admin-page'),
]