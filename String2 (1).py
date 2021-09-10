#문자열 인덱싱 - 문자마다 번호를 매길 수 잇음
a = "Life is too shrot, you need python"
print(a[3])
print(a[-3])

#문자열 슬라이싱 - 0~3까지 또는 전부
print (a[0] + a[1] + a[2] + a[3])
print (a[0:4])
print (a[19:-5]) #마지막 문자열 기준으로 -숫자만큼 슬라이싱

#문자열 바꾸기
# a[0:3] = "tree" //이럴경우, 오류가 난다. 만약 바꾸려면 아래 참조
print ("Tree" + a[4:])

#문자열 포맷팅
# %s - 문자열/ %c - 문자1개/ %d - 정수/ %f - 부동소수/ %o - 8진수/ %x - 16진수 / %% - Literal%(문자 '%' 자체)
k=10.5
print ("%d %s %f" %(5, "더하기", k))

#문자열%를 쓸려면 %%로 쓰기
print ("%f%%" %k)

#쓰여진 숫자만큼 띄어쓰기가 됨
print ("%10s" %"hi")
print ("%-10sjane" %'hi')

#소숫점 자리수 표현
print ("%0.4f" %3.142134234)
print ("%10.4f" %3.142134234) #소수점 넷째자리까지 표기하고 전체 10개의 문자열 표기

#format 함수 활용하기 //문자열로 포맷 바뀌어서 출력
print ("I ate {0} apples, so I was sick for {1} days.".format(k,"Three"))

#왼쪽정렬 & 오른쪽 정렬 & 가운데 정렬
print ("{0:<10}".format("hi"))
print ("{0:>10}".format("hi"))
print ("{0:^10}".format("hi"))

#공백 채우기
print ("{0:=^10}".format("hi"))
print ("{0:!^10}".format("hi"))

#소수점 표현
y = 3.42134234
print ("{0:0.4f}".format(y))
print ("{0:10.4f}".format(y))

#{문자} 표기
print ("{{Variable}}".format())

#f문자열 포매팅
age =29
d = {'name':'홍길동','age':30} #딕셔너리 기법이며,작은 따옴표로 맞춰야함/ 큰따옴표 테스트시 안됨
print (f"나는 내년이면 {age+1} 살이 된다.")
print (f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.") 

