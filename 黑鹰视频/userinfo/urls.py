from django.conf.urls import url
from userinfo import views

urlpatterns = [
    url(r"^login/$", views.login_),
    url(r"^loginin/$", views.loginin),
    url(r"^registerin/$", views.registerin),
    url(r"^logout/$", views.Logout, name='Logout'),
]
