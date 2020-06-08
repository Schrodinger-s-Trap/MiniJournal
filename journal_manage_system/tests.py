from django.test import TestCase

# Create your tests here.
from .models import Catalog


class ModelTest(TestCase):
    def setUp(self):
        new_item = Catalog(journal_name='test_journal', cnsn='cnsn', issn='issn', postcode='postcode')
        new_item.publisher = {'publisher': '测试出版社'}
        new_item.save()

    def test_catalog(self):
        for e in Catalog.objects.filter(issn='issn'):
            publisher = e.publisher
            print(type(publisher), publisher)
