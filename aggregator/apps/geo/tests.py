import pytest

from .models import City


# @pytest.mark.django_db()
# def test_cyty(f_city):
#     cities = City.objects.all()
#     assert len(cities) == 1
#     for city in cities:
#         assert city.name == f_city.name
#         assert city.domain_name == f_city.domain_name
#         assert city.slug == f_city.slug
