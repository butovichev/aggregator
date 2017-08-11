from urllib.parse import urlparse

from django.http import Http404

from aggregator.apps.geo.models import City


class SubDomainNameMiddleware:
    def process_request(self, request):
        url = urlparse(request.build_absolute_uri())
        subdomain = url.hostname.split('.')[0]
        cities = City.objects.all()

        if subdomain not in [city.domain_name for city in cities]:
            raise Http404
        else:
            request.city = subdomain
