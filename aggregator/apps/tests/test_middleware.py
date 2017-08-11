import pytest
from django.http import Http404
from aggregator.subdomains_name import SubDomainNameMiddleware


@pytest.mark.parametrize("subdomain_name,result", [
    ("msk", True),
    ("spb", True),
    ("xxx", False),
])
def test_sub_domain_name_middleware(db, request, subdomain_name, result):

    def build_absolute_uri():
        return 'http://{}.foo.ru'.format(subdomain_name)

    middleware = SubDomainNameMiddleware()

    request.build_absolute_uri = build_absolute_uri

    if not result:
        with pytest.raises(Http404):
            middleware.process_request(request)
    else:
        middleware.process_request(request)
        assert request.city == subdomain_name
