import pytest

from .models import Article


@pytest.mark.django_db()
@pytest.fixture(scope='function')
def f_article(f, user_staff, city_msk):
    data = {
        'author': user_staff,
        'title': f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)[:50],
        'text': f.paragraphs(nb=3, ext_word_list=None)[:50],
        'city': city_msk,
    }
    article = Article(**data)
    article.save()
    return article


@pytest.mark.django_db()
def test_article(f_article, city_msk):
    articles = Article.objects.filter(city__domain_name='msk')
    assert len(articles) == 1
    for article in articles:
        assert article.author == f_article.author
        assert article.title == f_article.title
        assert article.city == city_msk


    articles = Article.objects.filter(city__domain_name='xxx')
    assert len(articles) == 0


