'''
Created on 2019. 3. 31.

@author: A
'''
from django.forms.models import ModelForm
#django에서 기본적으로 제공하는 회원관리 어플리케이션
#에 있는 models.py에 접근해 회원클래스 임포트
from django.contrib.auth.models import User
from django import forms

#회원가입에 사용할 폼
class SignupForm(ModelForm):
    #모델클래스에 없는 입력양식 생성
    #forms에 들어있는 XXXXField 객체를 클래스변수에 저장해서 구현
    #모델클래스 구현에 사용했던 클래스명과 유사하나, 내부기능이
    #다르기 때문에 주의해야함
    password_check = forms.CharField(max_length=100,
                                     widget=forms.PasswordInput())
   
    #field_order : 입력양식의 순서를 저장하는 변수
    #리스트 타입으로 변수명을 문자열로 저장
    field_order = ['username','password','password_check',
                   'last_name','first_name','email']
    
    #forms에 들어있는 XXXXInput 객체를 widget으로 지정하면
    #해당 타입으로 입력양식이 생성됨
    #forms.PasswordInput : 입력한 데이터가 숨겨지도록
    #비밀 처리해주는 위젯
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password_check'].label = '비밀번호 확인'
    class Meta:
        model = User
        #아이디, 비밀번호, 성, 이름, 이메일
        fields = ['username','password',
                  'last_name','first_name','email']
        #사용하는 변수에 적용할 위젯 저장 변수
        widgets = {
            'password':forms.PasswordInput()
            }
#로그인에 사용할 폼
class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets={
            'password' : forms.PasswordInput()
            }












