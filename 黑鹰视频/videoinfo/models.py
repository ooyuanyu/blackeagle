from django.db import models
from datetime import datetime


# Create your models here.


class VideoInfo(models.Model):
    video_name = models.CharField(max_length=50, verbose_name="视频名称")
    image = models.ImageField(max_length=100, upload_to='static/images/%Y/%m', verbose_name="视频图片")
    video_file = models.FileField(upload_to="static/video/")
    title = models.CharField(verbose_name='视频html.url', max_length=256)
    content = models.TextField(verbose_name="内容", blank=True, null=True)
    video_type = models.CharField(choices=(
        ("1", "综艺"), ("2", "电影"), ("3", "动漫"), ("4", "少儿"), ("5", "音乐"), ("6", "美剧"), ("7", "韩剧"), ("8", "体育"),
        ("9", "游戏"), ("10", "生活"), ("11", "科技"), ("12", "旅游")
    ), max_length=10)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    comment = models.TextField(verbose_name="视频评论", blank=True, null=True)

    class Meta:
        verbose_name = "视频内容"
        verbose_name_plural = verbose_name

    def video_detail_url(self):
        return "/videoinfo/video/?AV={}/".format(self.id)

    def __str__(self):
        return self.video_name
