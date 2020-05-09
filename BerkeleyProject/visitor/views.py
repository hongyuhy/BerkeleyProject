# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from enum import Visitor
import logging

logger = logging.getLogger("BerkeleyProject")
# Create your views here.


def home(request):

	if Visitor.Count in cache:
		count = cache.get(Visitor.Count)
	else:
		count = 0
	count = count + 1
	cache.set(Visitor.Count, count)
	# return HttpResponse("Invalid password!")
	return render(request, 'index.html', {"visitor_count": count})
