# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Magazine
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def all_magazines(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazines})