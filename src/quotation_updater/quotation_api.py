import requests
from django.conf import settings

from quotations.models import Quotation


def _get_quotation_json():
    url = settings.QUOTATION_REQUEST_URL
    r = requests.get(url)

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None


def update_quotations():
    json = _get_quotation_json()
    json_currencies = json["results"]["currencies"]
    if json is not None:
        try:
            print("Getting quotation")
            currencies = ["EUR", "USD", "BTC"]
            new_quotations = []
            for cur in currencies:
                new_quotation = Quotation()
                new_quotation.currency = cur
                new_quotation.buy = json_currencies[cur]["buy"]
                new_quotation.sell = json_currencies[cur]["sell"]
                new_quotation.variation = json_currencies[cur]["variation"]
                new_quotations.append(new_quotation)

            # Add all quotations
            print("Saving quotations %s")
            Quotation.objects.bulk_create(new_quotations)
        except Exception as e:
            print('%s' % e)
