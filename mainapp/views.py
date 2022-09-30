from mainapp.serializers import (
    Shop, ShopSerializer,
    Ticket, TicketSerializer
)
from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from django.core.paginator import Paginator


class ShopView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    filterset_fields = ['address',]
    ordering_fields = ['time_start', 'time_end',]
    search_fields = ['name', ]

    objects = ['shop', 'address',]
    p = Paginator(objects, 2)
    p.count





class TicketView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = DjangoFilterBackend, filters.SearchFilter
    filterset_fields = ['shop', ]
    ordering_fields = ['time_start', 'time_end', ]
    search_fields = ['shop__name', 'name', 'price', ]

