# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Orders
from . serializers import OrdersSerializer

class OrdersList(APIView):
    def get(self,request):
        orderis = Orders.objects.all()
        serializer=OrdersSerializer(orderis,many=True)
        return Response(serializer.data)
    def post(self):
        pass
