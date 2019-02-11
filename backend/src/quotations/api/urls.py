from django.urls import path

from .views import QuotationListView


urlpatterns = [
    path('', QuotationListView.as_view(), base_name="test"),
]
