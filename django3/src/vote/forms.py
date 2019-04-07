'''
<form> : HTML의 <form> 태그로 사용자가 웹서버에게 전달할
값들을 작성할 수 있는 공간을 생성해줌
<form> 태그 안에 <input> 태그를 작성해서 어떤 입력을 할수
있는지 지정할 수 있음
form태그의 속성으로 action과 method를 지정해야함
action : 사용자의 입력을 웹서버의 어느 url로 보낼것인지 지정
method : GET 또는 POST 방식을 지정

장고의 form : HTML의 <form>태그에 들어가는 <input>태그들을
관리할 수 있는 클래스/기능
모델클래스에 정의된 변수에 맞춰 <input>을 자동생성하거나 커스텀
입력공간도 생성할 수 있음
'''

from django.forms.models import ModelForm
from vote.models import Question, Choice
'''
ModelForm : 모델클래스를 기반으로 입력양식을 자동 생성할때 상속
            받는 클래스
Form : 커스텀 입력양식을 생성할 때 상속받는 클래스

기존의 기능 개발 순서
Model 클래스 정의 -> 뷰 함수/클래스 정의 -> HTML 코드 작성
->URL Conf 등록

변경
Model 클래스 정의 -> form클래스 정의 -> 뷰 함수/클래스 정의 -> HTML 코드 작성
->URL Conf 등록
'''

#Question 모델클래스와 연동된 모델폼클래스 정의
#Question 객체 추가/수정 때 사용
class QuestionForm(ModelForm):
    #Meta 클래스 : 연동하고자 하는 모델클래스에 대한 정보를
    #정의하는 클래스 (대문자 주의) 
    class Meta:
        #모델폼클래스가 Question모델클래스와 연동
        model = Question 
        #Question모델클래스의 변수중 title변수만 작성가능
        fields = ['title']
        #model, fields, exclude - 변수이름 주의
        #model : 연동하고자하는 모델클래스를 지정하는 변수
        #fields : 모델클래스에 정의된 변수 중 어떤 변수를
        #         클라이언트가 작성할 수 있는지 지정하는 변수
        #(iterable, list형태로 변수명을 문자열로 저장함)
        #exclude : 모델클래스에 정의된 변수 중 입력양식으로
        #만들지 않을 변수들을 지정하는 변수
        #fields나 exclude 중 하나만 사용
        
#Choice 모델클래스와 연동된 모델폼클래스 정의
#Choice 객체 추가/수정 때 사용
class ChoiceForm(ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        print(self.fields)
        self.fields['q'].label = '설문조사'
    class Meta:
        model = Choice
        fields = ['q', 'name']
        #exclude = ['votes']










