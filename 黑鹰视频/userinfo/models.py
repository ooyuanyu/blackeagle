from django.db import models
from datetime import datetime


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=40, null=False)
    userpassword = models.CharField(verbose_name='密码', max_length=40, null=False)
    isactive = models.BooleanField(verbose_name='是否激活', default=True)
    isdelete = models.BooleanField(verbose_name='是否删除', default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="注册时间")
    amount_of_money = models.IntegerField(default=0, verbose_name="充值金额")
    email = models.EmailField(verbose_name="邮箱地址")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    image = models.ImageField(upload_to="static/banner/%Y%m", verbose_name="轮播图",max_length=100)
    url = models.URLField(max_length=200,verbose_name="访问地址")
    index = models.IntegerField(default=100,verbose_name="循序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
