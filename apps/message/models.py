# -*- coding: utf-8 -*-
from django.db import models


class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, default="", max_length=100, verbose_name=u"主键")
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name  # verbose_name的复数仍然是它本身, 不用加s
        # db_table = "user_message"  # migrate时指定数据表的名字
        # ordering = ["-object_id"]  # 按照object_id逆序排列, 而不需要增加SQL order by语句
