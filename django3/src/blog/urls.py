'''
Created on 2019. 4. 6.

@author: A
'''
from blog.views import *
from django.urls.conf import path
app_name = 'blog'
#127.0.0.1:8000/blog/
urlpatterns = [
    #뷰클래스는 as_view함수를 호출해서 URL을등록
    #127.0.0.1:8000/blog/ 요청
    path('',Index.as_view(), name='index'),
    #path('',test, name='index')
    #DetailView 제네릭뷰는 pk라는 추가 매개변수를 사용함
    #127.0.0.1:8000/blog/게시물숫자/
    path('<>/', Detail.as_view(), name='detail'),
    #127.0.0.1:8000/blog/posting
    path('posting/', Posting.as_view(), name='posting')
    ]
 






