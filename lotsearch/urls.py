from django.urls import path
from .views import get_lot_by_id

urlpatterns = [
    path('lot/<int:idlot>/', get_lot_by_id, name='get_lot_by_id'),
]
