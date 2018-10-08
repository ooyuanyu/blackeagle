"""黑鹰视频 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from . import settings
import xadmin
from django.conf.urls import url, include
from xadmin.plugins import xversion
from userinfo import views


xversion.register_models()

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('xadmin/',xadmin.site.urls),
    url(r'^userinfo/', include('userinfo.urls')),
    url(r'^$', views.Banner_, name='index'),
    url(r'^videoinfo/',include('videoinfo.urls')),
    url(r'^search/', include("searchinfo.urls")),
]

# urlpatterns += static('/statics/',document_root=settings.STATIC_ROOT)
