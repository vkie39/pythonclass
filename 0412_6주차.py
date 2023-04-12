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


#--------------------------
lst.append("김밥")

#.remove()
print(lst)
lst.remove("김밥")
print(lst)