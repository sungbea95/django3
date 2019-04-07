from django.db import models

# Create your models here.
#질문(Question)
#질문 제목(CharField(100글자제한), 생성일(DateField)
#title, pub_date
class Question(models.Model):
    title = models.CharField('설문조사 제목',max_length=100)
    pub_date = models.DateField()
    def __str__(self):
        return self.title
    #모델클래스에 정의된 변수, 테이블이름 등을 처리할 때 사용
    class Meta:
        #ordering: 해당 모델클래스의 객체들을 정렬하는 방식을 지정
        #리스트형태로 정렬에 사용할 변수이름을 문자열로 작성
        #변수이름 앞에 -를 붙이면 내림차순으로 정렬
        ordering=['-pub_date']
#답변(Choice)
#답변 항목 내용, 투표수, 어떤질문에 연결되있는지처리
#name(CharField(50글자제한)), votes(IntegerField)
#q(ForeignKey(질문모델클래스와연결))
class Choice(models.Model):
    name = models.CharField('답변항목', max_length=50)
    #default : 객체 생성 시 기본값 설정하는 매개변수
    votes = models.IntegerField('투표 수', default=0)
    #Choice모델클래스가 Question모델클래스와 1:n관계를 가짐
    #Question객체가 삭제되면 연결된 Choice객체도 삭제됨(CASCADE) 
    q = models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    #ForeignKey : 다른 모델클래스의 객체와 연결할 수 있는 클래스
    #ForeignKey(연결할 다른모델클래스,on_delete=삭제방식)
    #Choice 모델클래스의 q변수는 연결된 Question객체와 동일함
    #-> Choice객체.q.title(또는 pub_date, id)변수를 접근할수있음
    #on_delete : 연결된 모델클래스의 객체가 삭제될때 어떻게처리
    #할지 지정하는 변수
    #on_delete = models.PROTECT : 연결된 모델클래스의 객체가
    #삭제되지 않도록 막아주는 기능
    #models.CASCADE : 연결된 모델클래스의 객체가 삭제되면 같이삭제
    #ex) 글을 삭제하면 글안에 댓글이 사라짐
    #models.SET_NULL : 연결된 객체가 삭제되면 아무것도 연결하지않은
    #상태 유지
    #models.SET(연결할객체) : 연결된 객체가 삭제되면 매개변수로 넣은
    #객체와 연결
    #models.SET_DEFAULT : 연결된 객체가 삭제되면 기본 설정된 객체와
    #연결 










