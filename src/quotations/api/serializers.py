from rest_framework import serializers

from quotations.models import Quotation


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = ('currency',
                  'buy',
                  'sell',
                  'variation',
                  'created_on'
                  )
