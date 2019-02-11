from django.urls import reverse, resolve


class TestUrls:

    def test_list_url(self):
        path = reverse('api/quotations')
        assert resolve(path).view_name == 'detail'
