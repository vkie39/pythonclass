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

# 2 - 2 추가하는 다른 방법
lec.update({'강의실':213, '교수':'이희진'})
print(lec)

#밸류값을 변경하는 방법 1
lec['인원'] = 20
print(lec)

#밸류 값을 변경하는 방법 2
lec.update({'인원':10})
print(lec)


# 2교시--------------------------------------------------------------------------
month = {1: '1월', 2:'2월', 3:'3월', 4: '4월', 5:'5월', 6:'6월', 'seven': '7월', 8:'8월', 9:'9월', 10: '10월', 11:'11월', 12:'12월'}
'''
#바라는 결과: 1월 \n 2월 \n ----- 12월 - 방법 1
for key in range(1, 13) : 
        print(month[key])

# 방법 2
for key in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 :
      print(month[key])

print(month.keys()) #dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(month.values()) #dict_values(['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'])
print(month.items()) #dict_items([(1, '1월'), (2, '2월'),--- (12, '12월')])

#3 month.keys() ---------> String 타입도 가능
for key in month.keys():
      print(month[key])

#4
for v in month.values():
      print(v)

#5
for item in month.items():
      print(item)

#6
#month.items()
for item in month.items():
      #item  - > (k1, v1) k1를 가져오면 key, v1를 가져오면 value.  k1 자리는 0, v1자리는 1
      print("keys: ", item[0])
      print("value: ", item[1])

for hoho in month:
      print(hoho)



print(month.get('seven')) # 1월 이라고 나온다.
print('\n')
print(month.get('key100')) #없다고 나온다. 
print('\n')

print(month['k1']) #키 에러
print('\n')
print(month['key100']) #키 에러
print('\n')


#dictionary 삭제
print(month)
print(month.pop('seven')) #지정한 키를 삭제
print(month)
print(month.popitem()) #맨 마지막 키를 삭제.
print(month)

'''
# 3교시 ------------------------------------------------------------------

#zip(), enumerate()
'''
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'e', 'f']
l3 = [9, 8, 7, 6, 5]

#zip()의 결과 :  [(1, 'a', 9), (2, 'b', 8), (3, 'c', 7)]
'''

#zip()
l1 = ['한식', '중식', '양식', '일식',  '분식']
l2 = ['전주식당', '전가복', '초밥집']
l3 = ['제육', '탕수육', '연어초밥']

z = zip(l1, l2, l3) #zip한 걸 z에 넣기
print(type(z))
print(z) #이렇게 하면 메모리 주소가 나옴
print(list(z)) #실질적 결과 도출

#dictionary
#list -> dictonary x
#l2 = 키, l3- value

z1 = zip(l1, l3)
print(dict(z1)) #남는 l1의 키는 프린트되지 않는다.

'''
z2 = zip(l1, l2, l3)
print(dict(z2)) #value에러 
#어떻게 고치나?
'''

z2 = zip(l1, zip(l2, l3))
print(dict(z2))

l4 = ['제육', '탕수육', '연어덮밥']

print(enumerate(l4)) #메모리주소 나옴
print(list(enumerate(l4))) #위 아래 둘 다 사용 가능  (리스트 안에 있는 내용은 튜플임)
print(dict(enumerate(l4)))

subject = ['파이썬', '자바', 'C++', 'AI', '알고리즘']
classroom = [101, 102, 103, 104, 105]
# 과목명을 입력받는다
# 조건: dictoionary로 변환해서 활용
# 조건2: 무한루프로 강의실을 알려줘라
# 조건3: quit이라는 단어가 들어오면 강의실 알려주는 시스템을 종료해라
# 다른 과목을 물어보면 몰라요 라고 대답할 것, 다시 입력하는 루프로 돌아감
# 해당 과목에 대한 강의실을 알려준다.
# continue, break 활용할 것

d = dict(zip(subject, classroom))
         
while 1 :
    c = input("과목명을 입력하세요")
    print(c)
    if c == 'quit':
        print("종료합니다.")
        break
     
    if c in d.keys() :#C가 d에 들어있는 값과 동일하면 넘겨줘라
        print("강의실은: ", d[c]) #출력

    else : 
        print('몰라요')
        continue