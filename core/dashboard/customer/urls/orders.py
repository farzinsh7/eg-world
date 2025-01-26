from django.urls import path
from .. import views


urlpatterns = [
    path("orders/list/", views.CustomerOrdersListView.as_view(), name="orders-list"),
]
