# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'capture/index.html')