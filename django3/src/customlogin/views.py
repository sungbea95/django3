from django.shortcuts import render
from customlogin.forms import SignupForm, SigninForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

#회원가입
#GET - 회원가입 입력할 수 있는 HTML파일 제공
#POST - 사용자 입력 기반의 회원 생성
def signup(request):
    if request.method == 'GET':
        f = SignupForm()
        return render(request, 'cl/signup.html',
                      {'form':f})
    elif request.method == 'POST':
        f = SignupForm(request.POST)
        #유효한 값으로 채워져있는지 확인
        #(아이디 중복, 비밀번호 형식이 올바른지, 이메일형식)
        if f.is_valid():
            #is_valid가 True인 경우, cleaned_data 변수로
            #사용자의 입력을 추출할 수 있음
            #비밀번호확인란과 비밀번호가 같은지 확인
            if f.cleaned_data['password_check'] == f.cleaned_data['password']:
                #회원생성
                '''
                회원생성을 위해 f.save()를 사용할 경우, 비밀번호가
                암호화되지 않은 상태로 데이터베이스에 저장되기때문에
                비밀번호 원본이 저장됨
                따라서 회원생성에 사용할 수 있는 별도의 함수를 사용해야함
                
                User : auth 어플리케이션에 구현된 모델클래스
                User.objects.create_user : 비밀번호를 암호화한 상태로
                회원을 생성하는 함수 
                '''
               
                new_user = User.objects.create_user(username=f.cleaned_data['username'],
                                                    email = f.cleaned_data['email'],
                                                    password = f.cleaned_data['password'])
                print('새 유저 : ', new_user)
                new_user.last_name = f.cleaned_data['last_name']
                new_user.first_name = f.cleaned_data['first_name']
                #수정사항(성, 이름 변수에 값변경)을 데이터베이스에 반영
                new_user.save()
                #회원생성 완료 HTML 전달
                return render(request,'cl/signupcom.html',
                              {'name' : new_user.username})
            else:#비밀번호입력이 다른경우에 대한 처리
                return render(request, 'cl/signup.html',
                              {'form':f, 'error':'비밀번호가 다릅니다.'})
        else:#유효하지 않은 입력값이 있을때의 처리
            return render(request, 'cl/signup.html',
                          {'form' : f, 'error': '형식이 맞지않습니다.'})
#로그인
#GET - 로그인에 관한 입력을 할 수있는 HTML전달
#POST - 사용자 입력과 같은 회원이 존재하는지 확인후 로그인
def signin(request):
    if request.method == 'GET':
        f = SigninForm()
        return render(request,'cl/signin.html',
                      {'form':f } )
    elif request.method == 'POST':
        #회원조회 하는 함수를 사용해 아이디와비밀번호가
        #동일한 회원이있는지 확인
        #is_valid를 사용해 유효성 검사를 할 경우,
        #아이디 중복에 걸려 항상 False가 뜸
        #따라서 오류가 발생했을때 입력을 전달하기 위한 폼객체생성
        f = SigninForm(request.POST)
        #POST변수에서 직접 데이터 꺼내기(아이디,비밀번호)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        #아이디랑 비밀번호가 일치하는 User 모델클래스 객체 추출
        #authenticate(username,password) : 비밀번호를 암호화하고
        #아이디와 암호화된비밀번호가 일치하는 User객체 추출
        #단, 아이디나 비밀번호가 틀린경우, None값을 반환함
        u = authenticate(username=id, password=pw)
        #회원정보가 u변수에 들어있는경우
        if u:
            #로그인 처리
            #login(request, u) : 해당 뷰를 요청한 클라이언트가
            #u에 저장된 User 객체정보를 저장하는 함수
            login(request, u)
            #nexturl : 이동할 URL주소를 저장하는 변수
            nexturl = request.POST.get('nexturl')
            if nexturl:
                return HttpResponseRedirect(nexturl)
            else:
                return HttpResponseRedirect(reverse('vote:index')) 
        #회원정보가 u변수에 없는경우(None) 
        else:
            return render(request,'cl/signin.html',
                          {'form':f,
                           'error':'아이디 또는 비밀번호가 틀렸습니다.'})


#로그아웃
def signout(request):
    #logout(request) : 요청한 클라이언트의
    #User 저장 변수 값을 삭제함
    logout(request)
    return HttpResponseRedirect(reverse('cl:signin'))






