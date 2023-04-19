li = [1, 2, 3, 4] # 리스트
t1 = (1, 2, 3, 4, 2, 4, 3, 6 ,7, 8, 9, 2, 2, 2, 2, 2) #튜플
# 튜플은 수정할 수 없지만 리스트는 수정할 수 있다.

print(t1.count(2))
print(t1.index(2))

menu = ('아메', '라테', '유자차') 
#튜플을 수정하기 위해서는, 튜플을 새로 만들거나 리스트로 바꾼 다음 수정한다. 
menu1 = list(menu)
print(menu1)
menu1.append('아이스티')
print(menu1)
menu = tuple(menu1)
print(menu)

t2 = ()
print(t2)
t3 = 10, 20, 30, 40, 50 #이것도 튜플
print(t3)

t4 = 10
print(type(t4)) 
i4 = 10, 
print(type(i4)) #타입이 튜플이라고 나옴
print(t4)

lst = [10, 20, 30, 44, 5, 6, 1, 1]
lst.sort()

t3 = 1073, 203, 3, 40, 50 
print(sorted(t3))
print(t3)

for i in 1, 2, 3, 4, 5: #for문에 쓰인 1, 2, 3, 4, 5 배열은 튜플의 방법을 사용한 것이다.
    print(i)

#딕셔너리: 사전과 같이 키와 밸류로 이루어진 데이터
#d1 = {k1:v1, k2:v2, K3:v3} #딕셔너리는 중괄호
# {k1:v1, k1:v2} 는 오류가 나지만, {k1:v1, k2:v1}은 가능하다 (키 값은 중복이 불가, 밸류는 중복 가능)
student = {}
d2 = dict()

#사전에 값을 추가하는 법
# 1. 선언한다. 
student[101] = '홍갈동'
student[102] = '고길동'
student[103] = '박길동'
print(student)

print(student[101]) # student중에 101번인 학생
print("student[102]: ", student[102])
# print(student[0]) <- 키에러. 
# print(student['gkgk']) <-키에러.

# 2. 추가한다 
lec = {}
lec['강좌 명'] = '파이썬' #키와 밸류값 집어넣기
lec['개설년도'] = 2023 #리스트, int, 캐릭터 등 모두 들어갈 수 있다. 
lec['수강생'] = ['홍', '고', '김', '박']
lec['인원'] = 35
print(lec)

lec.update({'강의실':213, '교수':'이희진'})
print(lec)

#밸류값을 변경하는 방법 1
lec['인원'] = 20
print(lec)

#밸류 값을 변경하는 방법 2
lec.update({'인원':10})
print(lec)


