from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),

     path('initiate-mpesa-payment/', views.initiate_mpesa_payment, name='initiate_mpesa_payment'),
    path('mpesa-callback/', views.mpesa_callback, name='mpesa_callback'),
]
