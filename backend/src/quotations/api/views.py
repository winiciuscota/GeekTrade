from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

import requests

from quotations.models import Quotation
from quotations.api.serializers import QuotationSerializer


class QuotationListView(ListAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
