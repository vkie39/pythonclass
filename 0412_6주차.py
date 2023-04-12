#1. 빈 리스트를만들어서 하나씩 원소를 추가하는 방식
lst = []
print(type(lst))
lst.append('김밥')
lst.append('햄버거')
lst.append('감자튀김')
lst.append('탕수육')
print(lst)

# 리스트에 데이터 추가
lst.append("파스타")
print(lst)

# 데이터를 넣을 장소 지정해서 데이터 추가
lst.insert(0, "학식")
print(lst)
lst.insert(0, '서브웨이')
print(lst)

print("list에서 3번째에 있는 값입니다. ", lst[2])

#점심메뉴 출력하기 1
for i in range(len(lst)):
    print(lst[i])

#점심메뉴 출력하기 2
for i in lst:
    print(i)

lst.append("탕수육")
lst.insert(1, "탕수육")
print(lst)

print(lst.count("탕수육")) #탕수육이라는 단어 세기
print(lst.count("탕수육"), lst.index("탕수육")) #몇 번째에 있는지 알려주기

#slicing [::]
# lst[start:end:step] #step 수 만큼 뛰어넘어라. 
# lst[0, 10, 1] 
print(lst[::]) #전체
print(lst[:len(lst):1]) #전체
#40줄과 41줄은 뜻과 의미가 같다. 

print(lst[0:8:2]) #0~7번째 2칸식 뛰어넘기
print(lst[2:6:7]) #2~5번째 7칸 뛰어넘기
print(lst[3:7:1]) #3~6 번째 1칸씩 뛰어넘기
print(lst[::-1]) #거꾸로
print(lst[:6:3]) #3칸씩 0, 3 

'''
#--------------------------
lst.append("김밥")

#.remove()
print(lst)
lst.remove("김밥") #김밥이라는 모든 단어를 지우는 게 아니라 한 단어를 확인하고 지우면 끝남
print(lst)

# lst.remove("커피") #오류남 - value값이 없으니까
print("\n")
print("\n")



item1="커피"
item2="학식"
if item1 in lst:
    lst.remove(item1)
    print('커피존재함, ', lst)
else:
    print(item1, " - 존재 안 함")


if item2 in lst:
    lst.remove(item2)
    print(item2, "존재함")
    print(lst)



print("\n")
print("-------------------------")
print("\n")

#pop() : 데이터를 꺼내서 없앰
print(lst)
print("lst.pop(): ", lst.pop()) #() 괄호가 비어있으면 맨 뒤에 있는 게 지정됨
print(lst)
print("lst.pop(): ", lst.pop())
print(lst)
print("lst.pop(0): ", lst.pop(0)) #자리 위치 지정
print(lst)

'''

print("\n")
print("-------------------------")
print("\n")

dessert = ["케이크", "커피", "우유", "와플"]
print(dessert)
lst.extend(dessert) #lst에다가 dessert 리스트를 추가.
print(lst)

x="15" #string
print(type(x))
print(int(x) + 1) #16
print(x + "1") #151
print(type(x)) #어떤 타입?


print("\n")
print("-------------------------")
print("\n")


l1=["apple", "banana", 'orange', 'grape', 'peach', 'strawberry', 'melon']

#int, float, print 등은 타입을 바꿔주지 않는다.
#sorted() 도 바뀌지 않는다. 하지만, 리스트.sort ex) dessert.sort()는 바꿔준다. 

#sorted() vs sort() 


#(1) sorted()
'''
print(l1)
print(sorted(l1))
print(l1)

#(2) sort()
print("\n")
print("===========l1.sort( 실행 )================")
print("\n")


print(l1)
l1.sort()
print(l1)

'''

#reverse()
print(l1)
l1.reverse()
print(l1)

#clear - 비어있다.
l1.clear()
print(l1)

'''
del l1 #메모리에서 지워짐, NameError
print(l1) 
'''

print("\n")
print("-------------------------")
print("\n")


#리스트 컴프리핸션
#리스트를 선언할 때 짧게, 빠르게, 간결하게 하고 싶다. 

#0 ~ 10까지 숫자가 있는 리스트 선언
# 1) 그냥 선언
l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("l2 : ", l2)
# 2) for문으로 append
l3=[]
for i in range(11) : 
    l3.append(i)
print("l3: ", l3)

# 3) 리스트 컴프리핸션
l4 = [ i for i in range (11)]
print("14: ", l4)

print("\n")
print("-------------------------")
print("\n")

# 4) 0 - 10 까지의 숫자의 제곱을 리스트에 넣어라
square = [i**2 for i in range(11)] # 맨 앞: 진짜 넣어줄 데이터, for문: 반복
print("제곱: ", square) 

# 5) 0 - 10 까지 숫자의 3배수 리스트에 넣어라
drainage = [i*3 for i in range(11)]
print("삼배수: ", drainage)

# 6) hello 를 10번 넣어라
hello = ["hello" for i in range(10)]
print("helo : ", hello)

# 7) 0 - 10까지 짝수들의 제곱을 리스트에 넣으시오. 
list = [i**2 for i in range(11) if i %2 == 0] # 제곱을 구해주는데, 그게 if문에 맞으면 그렇게 해줘!!
print(list)

list2 = [i**2 for i in range(11) if i %2 == 0 if i%3==0 ]
print(list2)



print("\n")
print("-------------------------")
print("\n")



#list를 복사해보쟝
a = [0, 4, 16, 36, 64, 100]

#shallow copy : 메모리 주소를 공유 
b = a # 이 뜻은 a와 같은 주소값을 가리키게 하는 것.  

a.pop()
print(a)
print(b)  
print("a id b: ", a is b) 
# 값 똑같음

b.append("3333")
print(" === after b.append(333)=== ")
print('a : ', a)
print('b : ', b)
#값을 바꿔도 똑같음

#deep copy
c = a[:] #a[:] 방식 1
print("a: ", a)
print("c: ", c)

#방식 2
c=a.copy()
#방식 3
c=list(a)

#딥 카피 했다

#a.pop() , 데이터 변화
a.pop()
print("=== after a.pop() === ")
print("a: ", a)
print('b : ', b)
print("c: ", c)


#a.append 데이터 변화
a.append(555)
print("=== after a.pop() === ")
print("a: ", a)
print('b : ', b)
print("c: ", c)


'''
시험 범위: chapter6까지
'''