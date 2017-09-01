# -*- coding:utf-8 -*-
# @author:sumin
from django.db import models

# Create your models here.
class Con(models.Model):
    content_list = models.CharField(max_length=500, verbose_name=u'事项内容')
    flag = models.BooleanField(default=False, verbose_name=u'是否完成')
    pubdate = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')

    class  Meta:
        verbose_name = '待办事项'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content_list


