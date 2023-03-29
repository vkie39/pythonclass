# 0329
'''
print("안녕하세요")
print(3)
print(10, 6)

var = "안녕"
print(var)
print(type(var))
print(type(3))

var1 = 3 #서로의 자리를 바꾸면 에러남
height = 180
weight=50
radius = 
'''

'''
a = 3
b = 10

c = a + b
a = c
a = a + b
a += b

a*=b 

print ("a : ", a)
'''
'''
a = 2
b = 3
a **= b
print(a)
'''

'''
name = input("이름이 뭔가요?")
print("제 이름은 ", name, "입니다. ")
age = input("나이는?")
print("나이는", age , "입니다.")
print ("아버지 나이는", int(age) + 30, "입니다. ")
print(type(age))
int("30")
float("20.6")
str(30)
print("김민수")
'''

'''
celsius = 37
fahrenheit = celsius * 9/5 + 32
print('섭씨: ', celsius , ',', '화씨: ', fahrenheit)
print('섭씨: ',  celsius, ',', "화씨: ", fahrenheit)

distance = 384400
unit = 10000
manUnit, remainder = divmod(distance, unit)
print('지구에서 달까지의 거리: ', manUnit, '만', remainder, '킬로미터')
'''
'''
a = "python"
b = "동양미래대학교"
print(a[0], ' ', a[1], '...', a[5])
print("python"[0], ' ', "python"[1], '...', "python"[5])
print(len(a))
print(b[0], ' ', b[1], '...', b[5])
print("동양미래대학교"[0], ' ', "동양미래대학교"[1], '...', "동양미래대학교"[5])
print(len(b))
'''
'''
print("동양미래대"[:])

school = "동양미래대"
print("school[:] : ", school[:])
print("school[0:3]:", school[0:3])
print('school[1:4]', school[1:4])
print('school[2:4]', school[2:4])
print("school[2:3]:", school[1:])

major="컴퓨터소프트웨어공학과"
print("\n")
print("school[:] : ", school[:])
print("school[0:len(school):2]:", school[0:len(school):2])
print('major[0:len(major):2]', major[0:len(major):2])
print('major[8:len(school)]', major[0:len(school)])
print("major[:15:4]:", major[:15:4])

print('동양미래대학교'[5:0:-1])
print('동양미래대학교'[-1:-7:-1])
'''
'''
print("hello \n world")
print("hello \t world")
print("hello \b world")
print("hello \v world")

str_a="하하하"
str_b="호호호"
print(type(str_a))
str_b.find
str_a.replace("하", '호')
print(str_a.replace("하", "호"))
str_a=str_a.replace("하", "호")
print("str_a: ", str_a)

str_c="안녕하세요. 파이썬 수업입니다. 파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬"
print(str_c.replace("파이썬", "자바", 5))
'''

'''
입력: 6자리 실수 222.788
출력: 실수의 각 자리 합을 출력한다. 2+2+2+7+8+9 => ??
input(), int(), str.replace()
'''


read=input("6자리 실수 입력: ")
read=read.replace(".", "")
print("read: ", int(read[0])+int(read[1])+int(read[2])+int(read[3])+int(read[4])+int(read[5]))