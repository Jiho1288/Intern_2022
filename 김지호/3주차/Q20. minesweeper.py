import random                       #random모듈 import

n = int(input("input="))            #n값에 input입력받음

result = ''                         #결과에 대한 문자열 초기화

for i in range(n):                  #for반복문을 이용하여 n번 만큼, 빈문자열에 .과*중에 랜덤한 값 추가
    a = random.choice("*.")
    result += a

print(result)


row = int(input("row="))            # 열과 행값을 각각 row와 column 변수애 입력
column = int(input("column="))
                                    
for j in range(row):                # 과제1에서 row값에 대해 반복문 추가
    result = ''
    for i in range(column):
        a = random.choice("*.")
        result += a

    print(result)


