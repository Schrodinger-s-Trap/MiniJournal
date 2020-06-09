from django.core import serializers

from . import models
import logging

logger = logging.getLogger(__name__)


def __recursive_filter(src: dict, dst: dict):
    try:
        assert src is None or type(src) is dict
        assert dst is None or type(dst) is dict
    except Exception as e:
        logger.error('failed to filter json field, exception is {}'.format(e))
        return False

    if src is None or len(src) == 0:
        return True
    if dst is None or len(dst) == 0:
        return False
    for key in src.keys():
        if key in dst:
            if src[key] == dst[key]:
                pass
            elif type(src[key]) is dict and type(dst[key]) is dict and __recursive_filter(src[key], dst[key]):
                pass
            else:
                return False
        else:
            return
    return True


def query_subscribe(**kwargs):
    try:
        query_set = models.Subscribe.objects.filter(**kwargs)
    except Exception as e:
        logger.error('failed to query subscribe table, exception is {}'.format(e))
        return None
    resp = []
    for e in query_set:
        resp.append({
            'postcode': e.postcode,
            'journal_name': e.journal_name,
            'date': e.date,
        })
    return resp


def update_subscribe(**kwargs):
    _id = kwargs.get('_id')
    if '_id' in kwargs:
        kwargs.pop('_id')
    if _id is None:
        try:
            obj = models.Subscribe.objects.create(**kwargs)
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update subscribe table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update subscribe table, exception is {}'.format(e))
            return None
    else:
        try:
            obj = models.Catalog.objects.get(id=_id)
            if 'journal_name' in kwargs:
                obj.journal_name = kwargs.get('journal_name')
            if 'postcode' in kwargs:
                obj.postcode = kwargs.get('postcode')
            obj.save()
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update subscribe table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update subscribe table, exception is {}'.format(e))
            return None


def query_catalog(**kwargs):
    publisher_area = kwargs.get('publisher_area')
    publisher = kwargs.get('publisher')
    if 'publisher_area' in kwargs:
        kwargs.pop('publisher_area')
    if 'publisher' in kwargs:
        kwargs.pop('publisher')
    try:
        query_set = models.Catalog.objects.filter(**kwargs)
    except Exception as e:
        logger.error('failed to query catalog table, exception is {}'.format(e))
        return None

    resp = []
    for e in query_set:
        if __recursive_filter(publisher, e.publisher) and __recursive_filter(publisher_area, e.publisher_area):
            resp.append({
                'id': e.id,
                'journal_name': e.journal_name,
                'cssn': e.cnsn,
                'issn': e.issn,
                'postcode': e.postcode,
                'publisher_area': e.publisher_area,
                'publisher': e.publisher,
            })
    return resp


def update_catalog(**kwargs):
    _id = kwargs.get('_id')
    if '_id' in kwargs:
        kwargs.pop('_id')
    if 'publisher_area' in kwargs and type(kwargs.get('publisher_area')) is not dict:
        kwargs.pop('publisher_area')
    if 'publisher' in kwargs and type(kwargs.get('publisher')) is not dict:
        kwargs.pop('publisher')
    if _id is None:
        try:
            obj = models.Catalog.objects.create(**kwargs)
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update catalog table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update catalog table, exception is {}'.format(e))
            return None
    else:
        try:
            obj = models.Catalog.objects.get(id=_id)
            if 'journal_name' in kwargs:
                obj.journal_name = kwargs.get('journal_name')
            if 'cnsn' in kwargs:
                obj.cnsn = kwargs.get('cnsn')
            if 'issn' in kwargs:
                obj.issn = kwargs.get('issn')
            if 'postcode' in kwargs:
                obj.postcode = kwargs.get('postcode')
            if 'publisher_area' in kwargs:
                obj.publisher_area = kwargs.get('publisher_area')
            if 'publisher' in kwargs:
                obj.publisher = kwargs.get('publisher')
            obj.save()
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update catalog table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update catalog table, exception is {}'.format(e))
            return None


def query_register(**kwargs):
    journal_info = kwargs.get('journal_info')
    if 'journal_info' in kwargs:
        kwargs.pop('journal_info')
    try:
        query_set = models.Register.objects.filter(**kwargs)
    except Exception as e:
        logger.error('failed to query register table, exception is {}'.format(e))
        return None

    resp = []
    for e in query_set:
        if __recursive_filter(journal_info, e.journal_info):
            resp.append({
                'journal_name': e.journal_name,
                'journal_info': e.journal_info,
            })
    return resp


def update_register(**kwargs):
    _id = kwargs.get('_id')
    if '_id' in kwargs:
        kwargs.pop('_id')
    if 'journal_info' in kwargs and type(kwargs.get('journal_info')) is not dict:
        kwargs.pop('journal_info')
    if _id is None:
        try:
            obj = models.Register.objects.create(**kwargs)
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update register table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update register table, exception is {}'.format(e))
            return None
    else:
        try:
            obj = models.Register.objects.get(id=_id)
            if 'journal_name' in kwargs:
                obj.journal_name = kwargs.get('journal_name')
            if 'journal_info' in kwargs:
                obj.journal_info = kwargs.get('journal_info')
            obj.save()
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update register table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update register table, exception is {}'.format(e))
            return None


def query_content(**kwargs):
    journal_info = kwargs.get('journal_info')
    if 'journal_info' in kwargs:
        kwargs.pop('journal_info')
    paper_info = kwargs.get('paper_info')
    if 'paper_info' in kwargs:
        kwargs.pop('paper_info')
    try:
        query_set = models.Content.objects.filter(**kwargs)
    except Exception as e:
        logger.error('failed to query content table, exception is {}'.format(e))
        return None
    resp = []
    for e in query_set:
        if __recursive_filter(journal_info, e.journal_info) and __recursive_filter(paper_info, e.journal_info):
            resp.append({
                'journal_name': e.journal_name,
                'journal_info': e.journal_info,
                'paper_title': e.paper_title,
                'paper_info': e.paper_info,
            })
    return resp


def update_content(**kwargs):
    _id = kwargs.get('_id')
    if '_id' in kwargs:
        kwargs.pop('_id')
    if 'journal_info' in kwargs and type(kwargs.get('journal_info')) is not dict:
        kwargs.pop('journal_info')
    if 'paper_info' in kwargs and type(kwargs.get('paper_info')) is not dict:
        kwargs.pop('paper_info')
    if _id is None:
        try:
            obj = models.Content.objects.create(**kwargs)
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update content table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update content table, exception is {}'.format(e))
            return None
    else:
        try:
            obj = models.Content.objects.get(id=_id)
            if 'journal_name' in kwargs:
                obj.journal_name = kwargs.get('journal_name')
            if 'journal_info' in kwargs:
                obj.journal_info = kwargs.get('journal_info')
            if 'paper_title' in kwargs:
                obj.paper_title = kwargs.get('paper_title')
            if 'paper_info' in kwargs:
                obj.paper_info = kwargs.get('paper_info')
            obj.save()
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update content table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update content table, exception is {}'.format(e))
            return None


def query_borrow(**kwargs):
    journal_info = kwargs.get('journal_info')
    if 'journal_info' in kwargs:
        kwargs.pop('journal_info')
    try:
        query_set = models.Borrow.objects.filter(**kwargs)
    except Exception as e:
        logger.error('failed to query borrow table, exception is {}'.format(e))
        return None
    resp = []
    for e in query_set:
        if __recursive_filter(journal_info, e.journal_info):
            resp.append({
                'journal_name': e.journal_name,
                'journal_info': e.journal_info,
                'borrow_time': e.borrow_time,
                'return_time': e.return_time,
            })
    return resp


def update_borrow(**kwargs):
    _id = kwargs.get('_id')
    if '_id' in kwargs:
        kwargs.pop('_id')
    if 'journal_info' in kwargs and type(kwargs.get('journal_info')) is not dict:
        kwargs.pop('journal_info')
    if _id is None:
        try:
            obj = models.Borrow.objects.create(**kwargs)
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update borrow table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update borrow table, exception is {}'.format(e))
            return None
    else:
        try:
            obj = models.Borrow.objects.get(id=_id)
            if 'journal_name' in kwargs:
                obj.journal_name = kwargs.get('journal_name')
            if 'journal_info' in kwargs:
                obj.journal_info = kwargs.get('journal_info')
            obj.save()
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update borrow table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update borrow table, exception is {}'.format(e))
            return None


def query_user(**kwargs):
    try:
        query_set = models.User.objects.filter(**kwargs)
    except Exception as e:
        logger.error('failed to query user table, exception is {}'.format(e))
        return None
    resp = []
    for e in query_set:
        resp.append({
            'user_name': e.user_name,
            'user_id': e.user_id,
            'password': e.password,
            'authority': e.authority,
        })
    return resp


def update_user(**kwargs):
    _id = kwargs.get('_id')
    if '_id' in kwargs:
        kwargs.pop('_id')
    if _id is None:
        try:
            obj = models.User.objects.create(**kwargs)
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update user table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update user table, exception is {}'.format(e))
            return None
    else:
        try:
            obj = models.User.objects.get(id=_id)
            if 'user_name' in kwargs:
                obj.user_name = kwargs.get('user_name')
            if 'user_id' in kwargs:
                obj.user_id = kwargs.get('user_id')
            if 'authority' in kwargs:
                obj.authority = kwargs.get('authority')
            if 'password' in kwargs:
                obj.password = kwargs.get('password')
            obj.save()
            obj_json = serializers.serialize("json", [obj, ])
            logger.info('update borrow table successfully, obj is {}'.format(obj_json))
            return obj_json
        except Exception as e:
            logger.error('failed to update borrow table, exception is {}'.format(e))
            return None
