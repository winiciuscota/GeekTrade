from django.urls import path

from .views import (
    QuotationsView
)


urlpatterns = [
    path('', QuotationsView.as_view()),
]
