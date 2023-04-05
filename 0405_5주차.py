#문자열
'''
str="파이썬수업 씨수업 자바수업 파이썬수업 파이썬수업"
str2="파이썬수업, 씨수업, 자바수업, 이썬수업, 파이썬수업"

#replace
print(str.replace("파이썬", "자바", 3))

#count
print(str.count('파이썬'))

#split
print(str.split())
print(str2.split(","))
print(str2.split("업"))
'''

'''
#find, index
print("fnid: ", str.find("파이썬"), "index : ", str.index("파이썬"))
print(str.find("AI")) #둘 다 단어가 없다고 확인했지만, find는 단어가 없을 때 -1로 반환한다.
print(str.index("AI")) #둘 다 단어가 없다고 확인했지만, index는 단어가 없을 때 오류를 낸다.
'''
'''
#join
print("**".join(str))

#format 기억해야 함
#3+4=7
print(3, " + ", 4 , " = ", 7)

f="{} + {} = {}".format(3, 4, 3+4)
print(f)

f2="{0} = {1}  = {2}, {2}, {2}, {2}, {2}".format(3, 4, 3+4)
print(f2)

f3="{0:d} = {1:f}  = {2:f}, {2}, {2}, {2}, {2}".format(3, 4.0, 3+4.0) #형식을 나타내야 할 때.
print(f3)

f4="{0:10d} = {1:10f}  = {2:10.3f}".format(3, 4, 3+4) #공간을 띄우고 싶을 때
print(f4)

#10번 ppt

#bool
print(type(True), type(False))
'''

'''
a="hello"
bool()
bool(a) #어떤 변수를 boolean타입으로 바꿀 때
print(bool("hello"), bool("hi"), 
      bool(3), bool(1.2), bool(-3), bool(" "), bool(""), bool(0)) 
#string에서는 빈 문자열, int에서는 0만이 false로 나온다. 

print(int(True), int(False), str(True)) #위에 str변수를생성했기 때문에 typeerror가 나온다. 

'''
'''
#2교시, 반복문
h=9
if h<12 :
    #h가 12보다 작을 때
    print("오전 ", h, "가 12보다 작다")

elif 12<h<18: 
    print("오후 ", h, "는 12보다 크고 18보다 작아요 ")

else: 
    #실행문 2
    #h가 12보다 크다.
    print("저녁 ", h, "는 18보다 크다. (크거나 같다) ")

'''
'''
#if, elif, else
lunch = input("밥 먹을래?")

print("밥먹을래? ")
if lunch == 'yes':
    print('밥을 먹고싶군요')
    cafeteria=input('학식? ')
    if cafeteria == "yes" :
        print("8호관 1층으로 ")
    else: 
        print("학식을 싫어하는군요")
        subway = input("subway? ")
        if subway == "yes" :
            print("8호관 1층으로 고고")
        else:
            print("subway를 싫어하는군요")
else: 
    print("밥먹기 싫군요")

'''
'''
#for, while

for i in 1, 2, 3, 4, 5, 6 : 
    print("i : ", i)

for a in 10, 30, 52334, 1352 : 
    print("a: ", a)

for i in range(0, 20, 1): #i는 20번 늘어나는데, 1씩 늘려줭
    print("i : ", i)

for i in range(20): #기본값으로
    print("i: ", i)

for i in range(1, 10, 1):
    print("i: ", i)
'''
'''
#1부터 10까지 늘어나라ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
sum=0
for i in range(1, 11, 1):
    sum+=i
    print(sum)
# 원한다면 할 수 있는 부분 :
else: 
    print("for문이 정상저긍로 종료되었습니다. ")

#혹은
print("완전바깥. 정상종료되었습니다. ")

#while
n=0
while n<10 : 
    print("n :", n)
# 위의 반복문은 무한반복
'''
'''
n=0
sum=0
while n<10:
    sum+=n
    print('n: ', n)
    print(n, "번째 sum: ", sum)
    n+=1
print("while 밖에서 sum의 값: ", sum)

while True:
    print("무한루프")

while False:
    print("실행이 되지 않음")

while False:
    print("실행이 되지 않음")
while 0:
    print("실행이 되지 않음")

print("while 0 다음 줄입니다. ")

'''

#break continue
#단어 입력을 위한 무한 루프를 받는다.
#그 글자를 3번 써줌
#'exit' ->루프를 끝내고 종료
#'apple' -> 3번 안 쓰고 다시 단어 입력 받음

'''
while True:
    word=input("단어를 입력하시오. ")
    if word == 'exit':
        print("종료")
        break
    elif word == 'apple':
        print("단어 다시 입력: ")
        continue
    else:
        for i in range(3):
            print(word, end=" ")
        print('해당단어 끝')
'''

'''
import random
print(random.randint(0, 10))
'''

from random import randint
print(randint(0,100000))

#놀이동산 놀이기구 탑승 문제
#총 정원 4명
#정원이 차면, 놀이기구 시작
#정원이 키 150 이상만 탈 수 있음
#사람들한테 키 물어보고 탑승시키시오.
#150이상 4명이 되면 놀이기구 시작

print("놀이동산 놀이기구 탑승 ")
people=0
150
while people < 4 :
    ki = input("키가 몇이에요? ")
    if 150 <= int(ki):
        print("탑승 가능합니다. ")
        people+=1
    else:
        print("키를 더 키우세요")
else:
    print('정원 마감, 놀이기구 시작')
