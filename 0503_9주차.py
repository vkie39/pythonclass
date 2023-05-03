# 함수 이름: addthere , 기능: 3을 더함
#def function_name(intput1, input2, input3) :
    

def addthree(num):
    return num+3

result = addthree(100) #result = 103으로 정의됨
print(result) #혹은
print(addthree(100)) #로 정의할 수 있다.;;

def printaddthree(num):
    print(num+3)
printaddthree(100)

#function 작성 - function1- 사랑 이름 2개 입력받아서 안녕!사람1, 안녕 사람2 출력
def name(num1, num2):
    print("안녕!", num1, "안녕!", num2)
name("최서현", "최서연")

#function2 호출 - 숫자 두 개 입력받아서, 두 개의 합을 return 하는 함수를 정의하라
def addnum(num1, num2):
    return num1+num2
print(addnum(1, 2))

'''
인자가 몇개인지 모르지만 모든 인자를 합해 return
'''
def mysum2(*numbers):
    result = 0
    for num in numbers:
        result = result+num

    return result
print(mysum2(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))

lst1 = [10,10,10,10,10,10,10,10]
lst2=[10,10,10,10,10,10,10,10,10,10,10,10]
print(mysum2(*lst1))
print(mysum2(*lst2))

#메뉴 = 가격, 출력해주는 function
def cafe(**keyvalue):
    #수행문 menu와 가격을 출력하라
    for key in keyvalue: #아메, 라테, 핫초코
        print(key, " ", keyvalue[key])

cafe(아메 =  2000, 라테 = 3000 , 핫초코 = 5000)
print("===============")
cafe(아메 =  2000, 라테 = 3000)
print("===============")
cafe(아메 =  2000)

print("\n===============\n")

menu = {'아메': 2000, '라테' : 3000 , '핫초코': 5000}
cafe(**menu)

#############################################
#Lamda function 짧고 간결하게 쓰고 싶어서 개발된 function
#function 이름 짓기 싫을 때 

def addthree(num):
    return num + 3
addthree(100)
#위에걸 밑에 걸로 바꿈
print((lambda num:num+3)(100))

'''
#람다 응용 - 숫자를 입력받아서 10을 곱하고 return
print((lambda num2:num2*10)(int(input("숫자입력:"))))
'''


#람다 응용2 - 숫자를 두 개 입력, 두개를 곱해서 return
print((lambda n1, n2 : n1*n2)(3, 4))

###########################3교시###############################
'''
#map, filter
map(function, list)
map(function, [1, 2, 3 ,4, 5])
[function(1), function(2), function(3), function(4), function(5)]

#input - function, list
# output list하나

map(addthree[10, 20, 30, 40, 50])
[addthree(10), addthree(20), addthree(30), addthree(40), addthree(50)]
[13, 23, 33, 43, 53]
'''

def addthree(num):
    return num+3

#위에걸 맵 함수로 
print(list(map(addthree, [10, 20, 30, 40, 50])))
#이걸 람다로
print(list(map(lambda x : x+3, [10, 20, 30, 40, 50])))

#문제 1번: [1, 2, 3, 4, 5, 6]을 5배를 하고, 10을 더해서 결과를 list로 출력하시오.
def addfive(num):
    return (num*5)+10

#(1)
print(list(map(addfive, [1, 2, 3, 4, 5, 6])))
#(2) 이걸 람다로
print(list(map(lambda num:num*5+10, [1, 2, 3, 4, 5, 6])))

#문제 2번: 두개의 list를 하나씩 뽑아서, 두 개를 더해서 하나의 리스트로 만들어라. 
lst10=[10, 20, 30, 40, 50]
lst11=[1, 2, 3, 4, 5]

def mysum(n1, n2):
    return n1+n2

#(1)

#(2) 이걸 람다로

#filter - 조건 만족하면 결과물에 포함 아니면 포함 x
#filter(function, list) #map(function, list) - 쓰는 방법은 똑같음

def positive(x): 
    if x> 0:
        return True
    else:
        return False
print(list(filter(positive, [10, -2, 3, -5, 9])))

#이걸 한 문장으로

def positive2(x):
    return x>0

#밑의 내용은 똑같음.
print(list(filter(lambda x:x>0, [-3, 2, 10, -6, -22, 11])))

def is_even(x):
    if x % 2 == 0:
        return True
    return False

#for반복문 이용
arr1 = []
for val in range(1, 11): #1~10까지
    if is_even(val):
        arr1.append(val)
 
print(f"arr function: {arr1}")

#filter 함수 이용
arr2 = list(filter(is_even, range(1, 11)))
print(f'arr filter:{arr2}')
