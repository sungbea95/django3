from django.shortcuts import render, get_object_or_404
from vote.models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
#질문 리스트
def index(request):
    #DB에 저장된 Question 객체 추출
    objs = Question.objects.all()
    #index.html 파일에 Question객체리스트 전달 및
    #클라이언트에게 html파일 전송
    return render(request,'vote/index.html',
                  {'objs' : objs})
#질문 선택 및 투표처리
#q_id : 사용자가 선택한 Question 객체의 id변수값
def detail(request, q_id):
    #웹 클라이언트의 요청방식에 따른 코드 처리
    #GET -> 설문조사 html 제공,
    #POST -> 실제 투표 반영
    #request.method : "GET" "POST" 중 웹클라이언트가 요청한
    #처리방식의 문자열이 저장됨
    if request.method == "GET":
        #get_object_or_404(모델클래스,조건)
        #모델클래스에 조건을 검색해 1개의 객체 추출
        #만약 객체가 없는경우, 클라이언트의 잘못된접근으로
        #판단해 뷰함수를 종료하고 404번에러코드를 전달하는 함수
        
        #Question객체 중 id변수 값이 q_id와 같은 객체 추출
        #없으면 404번 에러코드 전달
        obj = get_object_or_404(Question, id=q_id)
        
        '''
        모델클래스A의객체.모델클래스B_set : A모델클래스와
        B모델클래스가 1:n관계(외래키연결)인 경우, 해당 A객체와
        연결된 B객체들을 대상으로 get(),all(),exclude(),filter()
        함수들을 사용할 수 있음
        Question 모델클래스와 Choice 모델클래스는 1:n관계이므로,
        Question 객체들은 자신과 연결된 Choice 객체들을 대상으로   
        get,all,exclude,filter를 사용할 수 있음
        '''
        
        #obj(Question객체)와 연결된 Choice객체를 모두 추출
        c_list = obj.choice_set.all()
        print(c_list)
        return render(request,'vote/detail.html',
                      {'q' : obj, 'c' : c_list})
    #POST요청에 대한 처리(투표 반영)
    elif request.method == "POST":
        #a : Choice 객체 id변수값
        '''
        사용자의 입력데이터 추출방법
        request.GET  : 사용자가 GET방식으로 요청할때 넘어온 데이터가  
        저장된 변수(사전형)
        request.POST : 사용자가 POST방식으로 요청할때 넘어온 데이터가
        저장된 변수(사전형)
        '''
        #<form>에서 넘어온 a변수 값 추출
        c_id = request.POST.get('a')
        #id 값으로 Choice 한개 추출
        c = get_object_or_404(Choice, id=c_id)
        #투표수 증가
        c.votes += 1
        #데이터베이스 저장
        c.save() #변수값이 변경된 것을 데이터베이스에 알려줌
        #result 뷰의 링크를 전달
        #c.q : Choice 객체가 연결한 Question 객체
        #c.q.id : Choice 객체가 연결한 Question객체의id변수값
        url = '/vote/result/%d/' % c.q.id
        #HttpResponseRedirect(URL주소)
        #웹 클라이언트에게 다른 인터넷주소를 넘겨줌
        #웹 클라이언트는 넘겨받은 인터넷주소로 다시 요청
        return HttpResponseRedirect(url)
#설문 결과 출력페이지
def result(request, q_id):
    #Question 객체를 추출(id = q_id)
    q = get_object_or_404(Question, id=q_id)
    #result.html에 데이터 전송 및 클라이언트에게 전달
    return render(request,'vote/result.html',
                  {'q': q})


from vote.forms import QuestionForm, ChoiceForm
#날짜/시간 관련 함수
from _datetime import datetime
#로그인이 되있는 클라이언트만 뷰함수를 쓸수있도록설정
#데코레이터 : URLConf를 통해 View함수가 호출될때,
#뷰가 실행되기 전에 먼저 실행되는 함수

#데코레이터 적용 방식
#@데코레이터 함수 이름
#def 뷰함수(request):

#클래스 기반의 뷰는 데코레이터 대신에 XXXMixin 클래스를
#상속받아서 사용

#login_required: 클라이언트가 비로그인상태일때, 로그인페이지로
#이동하는 데코레이터 함수
#로그인페이지 URL을 setting.py에 LOGIN_URL 변수에 저장할 수 있음
from django.contrib.auth.decorators import login_required


#Question 객체 추가
@login_required
def qregister(request):
    #사용자의 요청방식을 구분
    #GET방식 -> HTML을 전달
    if request.method == "GET":
        #Form클래스 이용방법
        #객체 생성 후 as_p, as_table, as_ul 함수를
        #호출하면 <input>태그를 자동생성해줌
        form = QuestionForm()
        print(form.as_p())
        #입력양식을 행,열단위로 HTML코드 생성
        html = form.as_table()
        return render(request,'vote/qform.html',
                      {'form' : html})
    #POST방식 -> 사용자 입력기반의 Question객체 생성
    elif request.method == "POST":
        #request.POST : 사용자 입력 데이터 저장 변수
        #사용자가 보낸 데이터를 기반으로 QuestionForm
        #객체 생성
        form = QuestionForm(request.POST)
        #사용자가 보낸 데이터가 유효한 값인지 확인
        if form.is_valid():
            '''
            폼객체.is_valid() : 사용자 입력이 유효한경우 True반환,      
            추가적으로 cleaned_data 변수를 사용해 데이터를 추출할수있음
            만약에 유효한값이 아닌경우 False반환,
            사용자의 입력을 다시받을 수 있도록 HTML코드를 전달
            
            모델폼객체는 연동된 모델객체를 생성할 수 있음
            모델폼객체.save() : 반환값 생성된 모델객체.  
                내부적으로 데이터베이스에 새로운 객체가 저장됨
            현재 QuestionForm객체로 title변수만 값이 작성되있어
            데이터베이스에 바로 저장을 할 수 없음(pub_date변수값없음)
            
            모델폼객체.save(commit=False) : 데이터베이스에 저장하지않고,
            모델객체만 반환함
            '''
            #form 객체와 연동된 모델객체를 q변수에 저장
            #q : Question 객체를 저장한 상태
            q = form.save(commit=False)
            print('생성할 객체의 제목 ', q.title)
            print('id 변수값 : ', q.id )
            #새로 생성할 객체에 서버컴퓨터의 현재날짜를 저장
            q.pub_date = datetime.now()
            #객체를 데이터베이스에 저장
            q.save()
            print('객체 생성 후 id 변수값 : ', q.id)
            #reverse 함수 : 파이썬 코드내에서 별칭기반으로
            #URL을 찾을 수 있는 함수
            #reverse(별칭 문자열, args=(매개변수값,))
            #index 뷰함수 호출
            return HttpResponseRedirect( reverse('vote:index') )
        else:
            pass
            
#Question 객체 수정
@login_required
def qupdate(request, q_id):
    #수정할 대상을 추출
    #id가 q_id와 같은 값을 저장한 객체를 q변수에 저장
    q = get_object_or_404(Question, id=q_id)
    #GET - 수정 대상의 정보를 바탕으로 입력양식 제공
    if request.method == "GET":
        #instance 매개변수 : 데이터베이스에 저장된 객체를
        #연동할 수 있는 변수. 연동한 모델폼객체는 HTML코드로
        #변환 시, 기본값이 객체 변수값으로 채워져있음
        form = QuestionForm(instance = q)
        #동일한 폼객체를 사용하기 때문에 동일한 HTML파일을 사용함
        
        return render(request,'vote/qform.html',
                      {'form' : form.as_table()})
    #POST - 사용자가 입력한 데이터로 수정
    elif request.method == 'POST':
        #q 객체의 데이터를 사용자의 입력으로 덮어쓰기한 폼객체생성
        form = QuestionForm(request.POST, instance=q)
        #q변수에 저장된 값을 사용자 입력값으로 변경
        #Question 객체에 빈칸이 없으므로 바로 데이터베이스에 저장
        w = form.save()
        print('q변수의 id :', q.id)
        print('w변수의 id :', w.id)
        #detail 뷰함수로 이동
        #매개변수에 들어갈 값으로 w변수의 id값 전달
        return HttpResponseRedirect(
            reverse('vote:detail',args=(w.id,) ) )
#Question 객체 삭제
@login_required
def qdelete(request, q_id):
    #삭제 객체를 찾기
    q = get_object_or_404(Question, id=q_id)
    #삭제 함수(delete) 호출
    print('객체 삭제전 id변수:', q.id)
    q.delete()
    print('삭제후 id변수:',q.id)
    return HttpResponseRedirect(reverse('vote:index'))
    
#Choice 객체 추가
#GET - ChoiceForm 객체를 생성해 HTML파일에 전달
#POST - 사용자 입력을 기반으로 ChoiceForm 객체 생성 후
#데이터베이스에 저장. 비어있는 변수값이 없으므로 바로 저장
#index or detail URL 전달
@login_required
def cregister(request):
    if request.method =='GET':
        f = ChoiceForm()
        return render(request,'vote/cform.html',
                      {'f':f})
    elif request.method =='POST':
        f = ChoiceForm(request.POST)
        c = f.save()
        #index 뷰로 이동
        #return HttpResponseRedirect(reverse('vote:index'))
        #삭제한 Choice객체가 연결된 Question객체의 detail로 이동
        return HttpResponseRedirect(reverse('vote:detail', args= (c.q.id,) )) 
        
#Choice 객체 수정
#공통 : 수정할 대상을 추출
#GET - Choice 객체 기반으로 ChoiceForm객체 생성 후 HTML전달
#POST - Choice 객체+입력데이터 기반으로 ChoiceForm 객체생성
#바로 데이터베이스에 저장
#index 또는 detail로 이동 
@login_required
def cupdate(request, c_id):
    c = get_object_or_404(Choice, id = c_id)
    if request.method == "GET":
        f = ChoiceForm(instance = c)
        return render(request,'vote/cform.html',{'f':f})
    elif request.method =="POST":
        f = ChoiceForm(request.POST, instance = c)
        f.save()
        #index 뷰로 이동
        #return HttpResponseRedirect(reverse('vote:index'))
        #삭제한 Choice객체가 연결된 Question객체의 detail로 이동
        return HttpResponseRedirect(reverse('vote:detail', args= (c.q.id,) )) 
#Choice 객체 삭제
#삭제할 대상을 추출 후 삭제
#index 또는 detail로 이동
@login_required
def cdelete(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    c.delete()
    #index 뷰로 이동
    #return HttpResponseRedirect(reverse('vote:index'))
    #삭제한 Choice객체가 연결된 Question객체의 detail로 이동
    return HttpResponseRedirect(
        reverse('vote:detail', args= (c.q.id,) )) 











