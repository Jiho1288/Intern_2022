"""
-----------------  Question  -----------------
A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
버전은 다음처럼 "." 으로 구분된 문자열이다.
두 개의 버전을 비교하는 프로그램을 작성하시오.
ex) - 0.0.2 > 0.0.1
    - 1.0.10 > 1.0.3
    - 1.2.0 > 1.1.99
    - 1.1 > 1.0.1
----------------------------------------------
"""
# 과제 1
## input_1 = "1.0.2"
## input_2 = "0.9.1"
## 출력 : 1.0.2 > 0.9.1

a1 = input("Version1 : ")   # 각각의 버전 입력
a2 = input("Version2 : ")

list_a1 = a1.split('.')     # '.'을 기준으로 input 값의 문자열 분리 후 list 생성
list_a2 = a2.split('.') 

a= max(len(list_a1),len(list_a2)) - min(len(list_a1),len(list_a2))      # 두 list의 Element 갯수의 차

if len(list_a1) > len(list_a2):     # 두 list의 Element 갯수 일치 시키기 
    for i in range(a):              # ex) 2.0.1.2, 1.0.0 일때 1.0.0 -> 1.0.0.0
        list_a2.append('0')

elif len(list_a1) < len(list_a2):
    for i in range(a):
        list_a1.append('0')

for i in range(len(list_a1)):       # 두 input 값의 크기 비교 후 부호 반환
    if list_a1 == list_a2:
        sign = "="
        break

    elif int(list_a1[i]) < int(list_a2[i]):
        sign ="<"
        break

    elif int(list_a1[i]) > int(list_a2[i]):
        sign = ">"
        break

print(f'{a1}{sign}{a2}')        # 결과 출력

    

# 과제 2
## input_1 = "1.0"
## input_2 = "1.0.4"
## 출력 : 1.0 < 1.0.4

a1 = input("Version1 : ")   
a2 = input("Version2 : ")

list_a1 = a1.split('.')  
list_a2 = a2.split('.') 

a= max(len(list_a1),len(list_a2)) - min(len(list_a1),len(list_a2))

if len(list_a1) > len(list_a2):
    for i in range(a):
        list_a2.append('0')

elif len(list_a1) < len(list_a2):
    for i in range(a):
        list_a1.append('0')

for i in range(len(list_a1)):
    if list_a1 == list_a2:
        sign = "="
        break

    elif int(list_a1[i]) < int(list_a2[i]):
        sign ="<"
        break

    elif int(list_a1[i]) > int(list_a2[i]):
        sign = ">"
        break

print(f'{a1}{sign}{a2}')


    

# 과제3
## input_1 = ["0.1.0", "1.0.4.9"]
## input_2 = ["0.0.1", "1.04.9"]
## 결과 : 0.1.0 > 0.0.1, 1.0.4.9 < 1.04.9

a1 = input("Version1 : ")   # 각각의 버전입력
a2 = input("Version2 : ")

a1_1 = a1.split('"')    # '"'을 기준으로 input 값 분리 후 list 생성
a2_1 = a2.split('"')    # output : ['[', '0.1.0' ',' '1.0.4.9' ']' ]


for i_1 in range(1,5,2):    # list에서 버전 정보만 추출 후 버전 크기 비교 반복

    list_a1 = a1_1[i_1].split('.')      # '.'을 기준으로 버전의 문자열 분리 후 list 생성
    list_a2 = a2_1[i_1].split('.')

    a= max(len(list_a1),len(list_a2)) - min(len(list_a1),len(list_a2))      # 두 list의 Element 갯수의 차

    if len(list_a1) > len(list_a2):     # 두 list의 Element 갯수 일치 시키기
        for i in range(a):              # ex) 2.0.1.2, 1.0.0 일때 1.0.0 -> 1.0.0.0
            list_a2.append('0')
    elif len(list_a1) < len(list_a2):
        for i in range(a):
            list_a1.append('0')

    for i in range(len(list_a1)):       # 두 input 값의 크기 비교 후 부호 반환
        if list_a1 == list_a2:
            sign = "="
            break
        elif int(list_a1[i]) < int(list_a2[i]):
            sign = "<"
            break
        elif int(list_a1[i]) > int(list_a2[i]):
            sign = ">"
            break

    print(f'{a1_1[i_1]}{sign}{a2_1[i_1]}')      # 결과 출력