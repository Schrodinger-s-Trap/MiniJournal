from django.test import TestCase
from .utils import *


class ModelTest(TestCase):
    def setUp(self):
        pass

    def test_subscribe(self):
        obj = update_subscribe(journal_name='test_journal', postcode='postcode')
        if obj is not None:
            print(obj)
        obj = query_subscribe(date__range=['2020-06-9', '2020-6-29'])
        if obj is not None:
            print(obj)

    def test_catalog(self):
        print(query_catalog())
        publisher_area = dict(area={})
        publisher_area['area'] = dict(
            primary='中国',
            secondary='云南',
        )
        obj = update_catalog(journal_name='test_journal', cnsn='cnsn', issn='issn', postcode='postcode',
                             publisher={'publisher': '测试出版社'}, publisher_area=publisher_area, _id=None)
        if obj is not None:
            print(obj)
        obj = query_catalog(journal_name='test_journal', cnsn='cnsn', issn='issn', postcode='postcode',
                            publisher_area={'area': {'primary': '中国'}})
        if obj is not None:
            print(obj)
        obj = update_catalog(journal_name='yet another journal', _id=obj[0]['id'])
        if obj is not None:
            print(obj)
