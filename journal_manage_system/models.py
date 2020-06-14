import jsonfield as json_field
from django.db import models


# 期刊征订表
class Subscribe(models.Model):
    postcode = models.CharField(max_length=20)
    journal_name = models.CharField(max_length=50)
    date = models.DateField('订阅日期', auto_now_add=True)


# 期刊目录表
class Catalog(models.Model):
    journal_name = models.CharField(max_length=50)
    cnsn = models.CharField(max_length=20)
    issn = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    publisher_area = json_field.JSONField()
    publisher = json_field.JSONField()

    def __str__(self):
        return self.journal_name


# 期刊登记表
class Register(models.Model):
    journal_name = models.CharField(max_length=50)
    journal_info = json_field.JSONField()


# 期刊内容表
class Content(models.Model):
    journal_name = models.CharField(max_length=50)
    journal_info = json_field.JSONField()
    paper_title = models.CharField(max_length=70)
    paper_info = json_field.JSONField()


# 期刊借阅表
class Borrow(models.Model):
    user_id = models.BigIntegerField()
    journal_name = models.CharField(max_length=50)
    journal_info = json_field.JSONField()
    has_returned = models.BooleanField(default=False)
    borrow_time = models.DateTimeField('借阅日期', auto_now_add=True)
    return_time = models.DateTimeField('归还日期',)


# 用户信息表
class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    authority = models.SmallIntegerField()
