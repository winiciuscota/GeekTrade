from django.urls import path

from .views import QuotationListView


urlpatterns = [
    path('', QuotationListView.as_view(), name="quotation-list"),
    path('/', QuotationListView.as_view(), name="quotation-list"),
]
