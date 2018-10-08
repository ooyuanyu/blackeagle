from django.shortcuts import render, HttpResponse
from .models import VideoInfo
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from userinfo.models import Banner
# Create your views here.

video_ = VideoInfo()


def videolist_(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    return render(request, 'index.html')


def video(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    else:
        video_id = request.GET.get("AV")[:-1]

        video_ = VideoInfo.objects.get(id=video_id)
        return render(request, "Video.html", {'message': video_})




"""综艺"""


def Variety(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    variety_video = VideoInfo.objects.filter(video_type="1")

    paginator = Paginator(variety_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        varieties = paginator.page(page)
    except PageNotAnInteger:
        varieties = paginator.page(1)
    except EmptyPage:
        varieties = paginator.page(paginator.num_pages)
    return render(request, "Variety.html", locals())


"""电影"""


def Film(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    film_video = VideoInfo.objects.filter(video_type="2")

    paginator = Paginator(film_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator.page(paginator.num_pages)
    return render(request, "Film.html", locals())


"""动漫"""


def Comic(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    comic_video = VideoInfo.objects.filter(video_type="3")

    paginator = Paginator(comic_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        comics = paginator.page(page)
    except PageNotAnInteger:
        comics = paginator.page(1)
    except EmptyPage:
        comics = paginator.page(paginator.num_pages)
    return render(request, "Comic.html", locals())


"""少儿"""


def Children(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    children_video = VideoInfo.objects.filter(video_type="4")

    paginator = Paginator(children_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        childrens = paginator.page(page)
    except PageNotAnInteger:
        childrens = paginator.page(1)
    except EmptyPage:
        childrens = paginator.page(paginator.num_pages)
    return render(request, "Children.html", locals())


"""音乐"""


def Music(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    music_video = VideoInfo.objects.filter(video_type="5")

    paginator = Paginator(music_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        musics = paginator.page(page)
    except PageNotAnInteger:
        musics = paginator.page(1)
    except EmptyPage:
        musics = paginator.page(paginator.num_pages)
    return render(request, "Music.html", locals())


"""美剧"""


def American_TV(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    ameraican_tv_video = VideoInfo.objects.filter(video_type="6")

    paginator = Paginator(ameraican_tv_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        ameraican_tvs = paginator.page(page)
    except PageNotAnInteger:
        ameraican_tvs = paginator.page(1)
    except EmptyPage:
        ameraican_tvs = paginator.page(paginator.num_pages)
    return render(request, "American_TV.html", locals())


"""韩剧"""


def Korean_Drama(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    korean_drama_video = VideoInfo.objects.filter(video_type="7")

    paginator = Paginator(korean_drama_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        korean_dramas = paginator.page(page)
    except PageNotAnInteger:
        korean_dramas = paginator.page(1)
    except EmptyPage:
        korean_dramas = paginator.page(paginator.num_pages)
    return render(request, "Korean_Drama.html", locals())


"""体育"""


def Sports(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    sport_video = VideoInfo.objects.filter(video_type="8")

    paginator = Paginator(sport_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        sports = paginator.page(page)
    except PageNotAnInteger:
        sports = paginator.page(1)
    except EmptyPage:
        sports = paginator.page(paginator.num_pages)
    return render(request, "Sports.html", locals())


"""游戏"""


def Games(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    game_video = VideoInfo.objects.filter(video_type="9")

    paginator = Paginator(game_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, "Games.html", locals())


"""生活"""


def Life(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    life_video = VideoInfo.objects.filter(video_type="10")

    paginator = Paginator(life_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        lifes = paginator.page(page)
    except PageNotAnInteger:
        lifes = paginator.page(1)
    except EmptyPage:
        lifes = paginator.page(paginator.num_pages)
    return render(request, "Life.html", locals())


"""科技"""


def Science_And_Technology(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    science_and_technology_video = VideoInfo.objects.filter(video_type="11")

    paginator = Paginator(science_and_technology_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        science_and_technologys = paginator.page(page)
    except PageNotAnInteger:
        science_and_technologys = paginator.page(1)
    except EmptyPage:
        science_and_technologys = paginator.page(paginator.num_pages)

    return render(request, "Science_And_Technology.html", locals())


"""旅游"""


def Travel(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect("/userinfo/login/")
    travel_video = VideoInfo.objects.filter(video_type="12")

    paginator = Paginator(travel_video, 9)
    page = request.GET.get('page', 1)
    # currentPage = int(page)
    try:
        travels = paginator.page(page)
    except PageNotAnInteger:
        travels = paginator.page(1)
    except EmptyPage:
        travels = paginator.page(paginator.num_pages)
    return render(request, "Travel.html", locals())
