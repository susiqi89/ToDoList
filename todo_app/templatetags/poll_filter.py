# -*- coding:utf-8 -*-
# @author:sumin
from django import template
import datetime

register = template.Library()

@register.filter()
def pubtime_info(datetimes):
    attrs = (
        (60 * 60 * 24 * 365,u'年'),
        (60 * 60 * 24 * 30,u'月'),
        (60 * 60 * 24 * 7,u'周'),
        (60 * 60 * 24,u'天'),
        (60 * 60,u'小时'),
        (60,u'分钟'),
    )

    #不是datetime类型转换后与datetime比较
    if not isinstance(datetimes, datetime.datetime):
        datetimes = datetime.datetime(datetimes.year, datetimes.month, datetimes.day )

    #获取当前时间并与发布时间做比较，计算差值
    now = datetime.datetime.now()
    delta = now - datetimes

    #忽略毫秒
    before = delta.days * 24 * 60 * 60 + delta.seconds

    #刚刚过去的1分钟
    if before <= 60:
        return u'刚刚发布'
    for seconds, unit in attrs:
        cont = before//seconds
        if cont != 0:
            break
    return  str(cont) + str(unit) + u'前发布'
