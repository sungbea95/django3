"""django3 URL Configuration

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
from django.contrib import admin
from django.urls import path, include

#bookmark 폴더에 있는 views.py의 뷰함수 임포트
from bookmark.views import index, book_list, book_one

#urls.py : 웹클라이언트의 요청을 분석해 특정한 뷰를 호출하는 역할
#urlpatterns : URL과 뷰함수를 매칭해서 관리하는 변수
#path(추가URL, 호출할 뷰)
#등록한 URL들은 앞단에 http://127.0.0.1:8000/ 주소가 붙음
urlpatterns = [
    #http://127.0.0.1:8000/a1 -> 관리자사이트 뷰 호출
    path('a1/', admin.site.urls),
    #http://127.0.0.1:8000/ -> index 뷰 호출
    path('', index, name='main' ),
    #http://127.0.0.1:8000/list/ -> book_list 뷰호출
    path('list/', book_list),
    #http://127.0.0.1:8000/숫자/
    #->book_one 뷰호출, book_idx변수에 숫자값이 들어감
    path('<int:book_idx>/', book_one),
    #127.0.0.1:8000/vote 로 시작하는 URL들을
    #vote폴더의 urls.py에서 처리하도록 등록함
    path('vote/', include('vote.urls')),
    #127.0.0.1:8000/cl로 시작하는 URL들을
    #customlogin 폴더의 urls.py에서 처리하도록 등록
    path('cl/', include('customlogin.urls')),
    #social_django 어플리케이션의 하위 URLConf 등록
    #우리가 만든 어플리케이션이 아니므로 app_name변수에 어떤
    #값이 있는지 확인하기 힘듦
    #include함수의 namespace매개변수 : app_name변수를 무시하고
    #하위 그룹의 이름을 지정할 수 있음
    path('auth/', include('social_django.urls', namespace= 'social')),
    path('blog/',include('blog.urls'))
]

#사용자가 이미지,첨부파일 요청했을때,
#웹서버 컴퓨터에 저장된 파일을 클라이언트에게
#전달하도록 설정
#웹서버의 로컬하드디스크와 URL주소를 연동

#setting.py 변수값을 사용할 수 있도록 임포트
from django.conf import settings
#MEDIA_URL 과 MEDIA_ROOT를 연결하기위한 함수 임포트
from django.conf.urls.static import static
#웹클라이언트의 파일요청 URL 주소와
#실제 파일경로를 연동함
urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)






