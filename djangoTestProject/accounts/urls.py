from django.urls import path
import accounts.views

urlpatterns = [
    path('', accounts.views.home),
    path('products/', accounts.views.products),
    path('customer/', accounts.views.customer),
]
