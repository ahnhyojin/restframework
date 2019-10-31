from django.shortcuts import render, redirect
from .models import Music, Singer, Genre

from rest_framework import viewsets
from .serializers import MusicSerializer, SingerSerializer, GenreSerializer

class MusicView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class =  MusicSerializer

    def perform_create(self, serializer):
        serializer.save()

class SingerView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class =  SingerSerializer

    def perform_create(self, serializer):
        serializer.save()

class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class =  GenreSerializer

    def perform_create(self, serializer):
        serializer.save()



def index_view(request):
    musics = Music.objects.all()
    singers = Singer.objects.all()
    genres = Genre.objects.all()

    context = {
        'musics' : musics,                  # Key 값이 html에서 쓰임
        'singers' : singers,
        'genres' : genres,
    }

    return render(request, 'index.html', context)

def detail_view(request, pk):
    music = Music.objects.get(id=pk)

    context = { 'music' : music }
    return render(request, 'detail.html', context)

def create_view(request):
    if  (request.method == 'GET'):
        return render(request, 'create.html')

    elif (request. method == 'POST'):
        title = request.POST.get('title')
        singer_text = request.POST.get('singer')
        genre_text = request.POST.get('genre')
        released_at = request.POST.get('released_at')

        singer = Singer.objects.get(name = singer_text)
        genre = Genre.objects.get(name=genre_text)

        music = Music(title=title, singer=singer, genres=genre, released_at=released_at)  ##파란색은 models에 객채이름,폴인 키로 받아오기때문에 객체를 받아와서 새로운 객체를 만들고 저장해줘야함 

        music.save()

        return redirect('/core/')
        # 입력된 가수이름, 장르만 입력할 수 있게 create 함수를 구성한것

def update_view(request, pk):
    if  (request.method == 'GET'):
        music = Music.objects.get(id=pk)
        context = {
            'music' : music,
        }
        return render(request, 'update.html', context)

    elif (request. method == 'POST'):
        title = request.POST.get('title')
        singer_text = request.POST.get('singer')
        genre_text = request.POST.get('genre')
        released_at = request.POST.get('released_at')

        singer = Singer.objects.get(name = singer_text)
        genre = Genre.objects.get(name=genre_text)

        music = Music(id=pk, title=title, singer=singer, genres=genre, released_at=released_at)  ##파란색은 models에 객채이름,폴인 키로 받아오기때문에 객체를 받아와서 새로운 객체를 만들고 저장해줘야함 
                                                                                              # id = pk : 그 피케이 값에 저장해준다는 업데이트해준다는 의미
        music.save()

        return redirect('/core/' + str(pk))

def delete_view(request):
    music = Music.objects.get(id=pk)
    music.delete()

    return redirect('/core/')
    

    ## 이거 html에 구현 안함
    # 초록빛 @@@@@@ 이런거 여러개 생긴거 다시 생각해보기