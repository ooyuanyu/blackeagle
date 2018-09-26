from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q
import logging
from videoinfo.models import *
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def searchResult(request):
    if not request.session.get('user_name'):
        return HttpResponseRedirect('/', {'message': '请先登录'})
    else:
        if request.method == 'POST':
            searchcontent = request.POST.get('searchinfo')
            try:
                find_content = VideoInfo.objects.filter(Q(video_name__contains=searchcontent))
                if len(find_content) <= 0:
                    return render(request, 'index.html', {'messagenotfond': '没有要查找的内容'})
                else:
                    return render(request, 'searchresult.html', locals())
            except ObjectDoesNotExist as e:
                logging.warning(e)
            return render(request, 'index.html')