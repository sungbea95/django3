from django.db import models
'''
models.py : 모델클래스를 정의할 때 사용하는 파일
model : MTV 패턴중 하나로 데이터베이스에 데이터를 저장할
형식 정의 및 데이터 추가/수정/삭제/조회 기능 제공

model 클래스 개발 및 웹프로젝트 반영 순서
1)모델클래스 정의 시, models.Model 클래스 상속 후 정의
2)정의한 모델 클래스를 makemigrations 명령으로 migrations폴더에
migration 파일 저장
3) 저장된 migration 파일로 데이터베이스에 저장공간 생성
(manage.py 파일에 migrate 명령)

'''
#북마크를 저장할 모델 클래스
#즐겨찾기이름(파란글씨), 클릭 시 넘어갈 URL주소
class Bookmark(models.Model):
    #모델클래스에서 저장할 변수는 클래스 변수로 정의함
    #클래스변수에 models.XXXXField 클래스의 객체를 저장하는 것으로
    #저장공간 정의
    #CharField : 글자수 제한이 있는 문자열을 저장하는 공간
    #->max_length(필수) : 최대글자 수를 지정할 수 있는 매개변수
    name = models.CharField(max_length=100)
    #URLField : 인터넷주소(URL)을 저장하는 공간
    url = models.URLField()
    
    #def __str__ : 객체를 출력할때(print(객체))
    #표현방식을 처리하는 파이썬 클래스 함수
    def __str__(self):
        return self.name








