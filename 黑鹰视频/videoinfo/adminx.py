__author__ = 'yu'
__date__ = '2018/8/29 12:44'

from .models import VideoInfo
import xadmin


class VideoInfoAdmin(object):
    list_display = ["video_name", "image", "video_file", "content", "add_time", "fav_nums", "video_type",
                    "video_file", "id"]
    search_fields = ["video_name", "image", "content", "fav_nums", "comment", "video_type", "video_file", "id"]
    list_filter = ["video_name", "image", "content", "add_time", "fav_nums", "comment", "video_type",
                   "video_file", "id"]


xadmin.site.register(VideoInfo, VideoInfoAdmin)
