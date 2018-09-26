from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class BaseModel(models.Model):
    """
        基础模型
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    created_by = models.IntegerField(verbose_name="创建人ID")
    updated_by = models.IntegerField(verbose_name="修改人ID")
    is_active = models.BooleanField(default=True, verbose_name='是否正常')

    class Meta:
        abstract = True


class Alipay(BaseModel):
    """
        支付
    """

    subject = models.CharField(max_length=256, verbose_name="订单标题")
    out_trade_no = models.CharField(max_length=64, unique=True, verbose_name="唯一订单号")
    trade_no = models.CharField(default="", max_length=64, verbose_name="支付宝系统中的交易流水号")
    total_amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="订单的资金总额")
    return_url = models.CharField(max_length=500, verbose_name="支付完成同步跳转地址")
    notify_url = models.CharField(max_length=500, verbose_name="支付完成异步通知rpc地址")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    pay_nos = ArrayField(models.CharField(max_length=100), default=[], verbose_name='同一订单的支付ID数组')

    class Meta:
        verbose_name = "阿里支付"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)


class Wxorder(BaseModel):
    """
        订单
    """
    body = models.CharField(max_length=256, verbose_name="商品描述")
    out_trade_no = models.CharField(max_length=64, unique=True, verbose_name="订单号")
    transaction_id = models.CharField(default="", max_length=64, verbose_name="微信支付订单号")
    total_fee = models.BigIntegerField(verbose_name="订单的资金总额,单位为分")
    product_id = models.CharField(max_length=16, verbose_name="商品ID")
    notify_url = models.CharField(max_length=500, verbose_name="支付完成通知url")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    class Meta:
        verbose_name = "微信订单"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)


class Wxpay(BaseModel):
    """
        微信支付
    """
    out_trade_no = models.CharField(null=True, blank=True, max_length=64, verbose_name="订单号")
    pay_no = models.CharField(null=True, blank=True, max_length=64, unique=True, verbose_name="支付唯一订单号")
    code_url = models.CharField(null=True, blank=True, max_length=100, verbose_name="二维码地址")
    nonce_str = models.CharField(null=True, blank=True, max_length=32, verbose_name="随机字符串")

    class Meta:
        verbose_name = "微信支付"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)