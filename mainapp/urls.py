from rest_framework.routers import DefaultRouter as DR
from mainapp.views import *

router = DR()

router.register('shops', ShopView, basename='shops')
router.register('tickets', TicketView, basename='tickets')

urlpatterns = []

urlpatterns += router.urls
