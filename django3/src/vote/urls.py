'''
Created on 2019. 3. 24.

@author: user
'''
#서브 URL Conf를 만들어서 사용할 경우,
#app_name, urlpatterns 변수가 반드시 존재해야함
#app_name : 서브 URL Conf의 그룹명
#urlpatterns : path함수를 이용해 URL과 뷰함수 등록
from django.urls.conf import path
from vote.views import *

#기본 도메인 주소 : 127.0.0.1:8000/vote/
app_name = 'vote'
urlpatterns=[
    #127.0.0.1:8000/vote/
    path('', index, name='index'),
    #127.0.0.1:8000/vote/숫자/
    path('<int:q_id>/', detail, name='detail'),
    #127.0.0.1:8000/vote/result/숫자/
    path('result/<int:q_id>/',result, name='result'),
    #127.0.0.1:8000/vote/qr/
    path('qr/',qregister, name='qregister'),
    #127.0.0.1:8000/vote/qu/숫자
    path('qu/<int:q_id>/', qupdate, name='qupdate'),
    #127.0.0.1:8000/vote/qd/숫자
    path('qd/<int:q_id>/',qdelete,name='qdelete'),
    #127.0.0.1:8000/vote/cr/
    path('cr/', cregister, name='cregister'),
    #127.0.0.1:8000/vote/cu/숫자
    path('cu/<int:c_id>/', cupdate, name='cupdate'),
    #127.0.0.1:8000/vote/cd/숫자
    path('cd/<int:c_id>/', cdelete, name='cdelete'),
    ]








