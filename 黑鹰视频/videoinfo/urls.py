from django.conf.urls import url
from videoinfo import views

urlpatterns = [
    url(r"^videolist/$", views.videolist_),
    url(r'video/$',views.video),
    url(r"^variety/$", views.Variety),  # 综艺
    url(r'^film/$', views.Film),  # 电影
    url(r'^comic/$', views.Comic),  # 动漫
    url(r'^children/$', views.Children),  # 少儿
    url(r'^music/$', views.Music),  # 音乐
    url(r'^american_tv/$', views.American_TV),  # 美剧
    url(r'^korean_drama/$', views.Korean_Drama),  # 韩剧
    url(r'^sports/$', views.Sports),  # 体育
    url(r'^game/$', views.Games),  # 游戏
    url(r'^life/$', views.Life),  # 生活
    url(r'science_and_technology', views.Science_And_Technology),  # 科技
    url(r'^travel', views.Travel)  # 旅游
]
