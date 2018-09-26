__author__ = 'yu'
__date__ = '2018/9/12 10:36'

from django.conf import settings
from rest_framework import serializers

from pay_service.models import Alipay, Wxpay


class BaseSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT, read_only=True)
    updated_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT, read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = None


class AlipaySerializer(BaseSerializer):
    """
        阿里支付序列化类
    """

    class Meta:
        model = Alipay
        fields = "__all__"


class WxpaySerializer(BaseSerializer):
    """
        阿里支付序列化类
    """

    class Meta:
        model = Wxpay
        fields = "__all__"