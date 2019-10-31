"""drf_week1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import MusicView, SingerView, GenreView

music_list = MusicView.as_view({      ## 정보를 받아온다 
    'post': 'create',                    # 포스트는 create,get은 list
    'get': 'list',
})

music_detail = MusicView.as_view({
    'get': 'retrieve',                  # get은 retrieve, put은 update, delete삭제는 destroy(삭제)된다
    'put': 'update',
    'delete': 'destroy',
})


urlpatterns = format_suffix_patterns([    #format_suffix_patterns "/"뒤에 붙는 이거 안써도 되게 해주는 역할"
    path('admin/', admin.site.urls),
    # path('core/', include('core.urls')),
    path('musics/', music_list ),
    path('musics/<int:pk>/', music_detail ),
    # path('singers/', ),
    # path('genres/', ),
    #core아래 있으면 규칙이 충족되지 않음 이곳에 프로젝트 url에 써줘야함
])
