from blog.models import Post, PostImage, PostFile
from django import forms
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

#글쓰기에 사용할 폼클래스 - 모델폼클래스 상속
class PostForm(forms.ModelForm):
    #사용자가 첨부파일, 이미지를 업로드할 수 있도록
    #커스텀 입력양식 생성
    
    #이미지나 파일을 업로드하지않아도 글을쓸수있도록
    #커스텀 입력양식을 사용하는 것을 선택할 수있도록 설정
    #-> required 매개변수를 False값을 설정
    
    #하나의 파일업로드 입력양식에 여러개의 파일을
    #동시에 업로드할 수 있도록 위젯 설정
    #->ClearableFileInput 위젯을 사용
    files = forms.FileField(required=False,
        widget=forms.ClearableFileInput( attrs={'multiple':True} ) )      
    images = forms.ImageField(required = False,
        widget=forms.ClearableFileInput( attrs={'multiple':True} ))
    class Meta:
        model = Post
        fields = ['category','headline','content']

