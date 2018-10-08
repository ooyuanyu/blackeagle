__author__ = 'yu'
__date__ = '2018/8/29 8:37'

from .models import UserInfo,Banner

import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "黑鹰视频后台管理系统"
    site_footer = "黑鹰视频"
    menu_style = "accordion"


class UserInfoAdmin(object):
    list_display = ["username", "userpassword", "isactive", "isdelete", "add_time","email","amount_of_money"]
    search_fields = ["username", "userpassword", "isactive", "isdelete","email","amount_of_money"]
    list_filter = ["username", "userpassword", "isactive", "isdelete", "add_time","email","amount_of_money"]


class BannerAdmin(object):
    list_display = ["title","image","url","index","add_time"]
    search_fields = ["title","image","url","index"]
    list_filter = ["title","image","url","index","add_time"]


xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner,BannerAdmin)
