# -*- coding:utf-8 -*-
# @author:sumin\
from django.http import HttpResponse
from django.shortcuts import render

class CheckVersionsMiddleware(object):
    def process_request(self, request):
        if 'rv:11.0' in request.META['HTTP_USER_AGENT']:
            return render(request, 'version_error.html')
