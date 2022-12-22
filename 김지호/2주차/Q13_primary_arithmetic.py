"""
- 첫 번째 계산
  아이들은 여러 자리 숫자들을 더하기 위해서
  우에서 좌로 숫자를 하나씩 차례대로 더 하라고 배웠다.
  1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는 "한자리올림"연산을
  많이 발견하는 것은 중요한 도전이 된다.
  당신의 일은 교육자가 그들의 어려움을 평가하기 위하여,
  덧셈 문제들의 각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.

- 입력
  입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다.
  입력의 마지막 라인은 0 0 을 포한한다.

- 출력
  마지막을 제외한 입력의 각 라인에 대해서 당신은 두 숫자들을 더한 결과에서
  한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.

[입력 샘플]
123 456
555 555
123 594
0 0

[출력 샘플]
No carry operation
3 carry operation
1 carry operation
"""

"""
==========================================================================
# 입력값이 한개인 경우
==========================================================================
"""
print("***입력값이 한개일 경우***")

input_num = input("input=")         # input 된 값을 input_num 변수에 저장

input_list = input_num.split(" ")   # split 함수로 띄어쓰기를 기준으로 두 수를 구분 후 list에 저장

input_1 = input_list[0]             # 첫번째 값 input_1 변수에 저장
input_2 = input_list[1]             # 두번째 값 input_2 변수에 저장

input_1_list = list(input_1)        # 첫번째 값을 list로 분해
input_2_list = list(input_2)        # 두번째 값을 list로 분해


if len(input_1_list) > len(input_2_list):                       # 두 값의 자릿수가 다를때 if 문을 사용하여 자릿수 맞춰주기
    for i in range(len(input_1_list) - len(input_2_list)):      # 두 값을 비교해 자릿값이 적은 값의 앞 부분에 자릿수가 같아질 때까지 반복문을 활용하여 0 생성
        input_2_list.insert(0,"0")

elif len(input_1_list) < len(input_2_list):
    for i in range(len(input_2_list) - len(input_1_list)):
        input_1_list.insert(0,"0")


carry = 0                           # carry의 초기 값을 변수에 저장

for i in range(len(input_1_list)):                              # 반복문을 활용하여 각각의 자릿수에서 발생하는 캐리 값의 갯수를 세어줌

    if int(input_1_list[i]) + int(input_2_list[i]) >= 10:

        carry += 1

if carry ==  0:                         # carry가 0 일때 No carry operation 출력
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")  # 0이 아니면 carry 값을 그대로 출력


"""
==========================================================================
# 과제 1. 입력 값의 자릿수가 같을 때 한자리 올림 계산 횟수를 출력하시오.
## Input :  123 456
            555 555
            123 594
            0 0
## 출력 :   No carry operation
           3 carry operation
           1 carry operation
## 조건 1> 입력이 총 4번 완료된 후에 계산이 수행되도록 하세요.
## 조건 2> 입력값은 '123 456'의 형태로 받습니다.
==========================================================================
"""

print("\n***과제1***")                      # 4개의 input 값을 먼저 받은 후에 각각의 input 값에 대한 carry를 계산해줌

input_num_1 = input("input=")
input_num_2 = input("input=")
input_num_3 = input("input=")
input_num_4 = input("input=")


input_list_1 = input_num_1.split(" ")
input_list_2 = input_num_2.split(" ")
input_list_3 = input_num_3.split(" ")


input_1_1 = input_list_1[0]
input_1_2 = input_list_1[1]
input_2_1 = input_list_2[0]
input_2_2 = input_list_2[1]
input_3_1 = input_list_3[0]
input_3_2 = input_list_3[1]


input_1_1_list = list(input_1_1)           # 첫번째 input
input_1_2_list = list(input_1_2)

carry = 0

for i in range(len(input_1_1_list)):

    if int(input_1_1_list[i]) + int(input_1_2_list[i]) >= 10:

        carry += 1

if carry ==  0:
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")

##########################################

input_2_1_list = list(input_2_1)            # 두번째 input
input_2_2_list = list(input_2_2)

carry = 0

for i in range(len(input_2_1_list)):

    if int(input_2_1_list[i]) + int(input_2_2_list[i]) >= 10:

        carry += 1

if carry ==  0:
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")

###############################################

input_3_1_list = list(input_3_1)            # 세번째 input
input_3_2_list = list(input_3_2)

carry = 0

for i in range(len(input_3_1_list)):        

    if int(input_3_1_list[i]) + int(input_3_2_list[i]) >= 10:

        carry += 1

if carry ==  0:
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")

"""
==========================================================================
# 과제 2. 입력 값의 자릿수가 다를 때의 한자리 올림 계산 횟수를 출력하시오.
## Input : 13 452
           55 555
           1009 99
           0 0
## 출력 : No carry operation
         2 carry operation
         1 carry operation
## 조건 1> 입력이 총 4번 완료된 후에 계산이 수행되도록 하세요.
## 조건 2> 입력값은 '13 452'의 형태로 받습니다.
==========================================================================
"""

print("\n***과제2***")

input_num_1 = input("input=")
input_num_2 = input("input=")
input_num_3 = input("input=")
input_num_4 = input("input=")


input_list_1 = input_num_1.split(" ")
input_list_2 = input_num_2.split(" ")
input_list_3 = input_num_3.split(" ")


input_1_1 = input_list_1[0]
input_1_2 = input_list_1[1]
input_2_1 = input_list_2[0]
input_2_2 = input_list_2[1]
input_3_1 = input_list_3[0]
input_3_2 = input_list_3[1]


input_1_1_list = list(input_1_1)                                # 첫번째 input
input_1_2_list = list(input_1_2)

if len(input_1_1_list) > len(input_1_2_list):
    for i in range(len(input_1_1_list) - len(input_1_2_list)):
        input_1_2_list.insert(0,"0")

elif len(input_1_1_list) < len(input_1_2_list):
    for i in range(len(input_1_2_list) - len(input_1_1_list)):
        input_1_1_list.insert(0,"0")

carry = 0

for i in range(len(input_1_1_list)):

    if int(input_1_1_list[i]) + int(input_1_2_list[i]) >= 10:

        carry += 1

if carry ==  0:
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")

##########################################

input_2_1_list = list(input_2_1)                                    # 두번째 input
input_2_2_list = list(input_2_2)

if len(input_2_1_list) > len(input_2_2_list):
    for i in range(len(input_2_1_list) - len(input_2_2_list)):
        input_2_2_list.insert(0,"0")

elif len(input_2_1_list) < len(input_2_2_list):
    for i in range(len(input_2_2_list) - len(input_2_1_list)):
        input_2_1_list.insert(0,"0")

carry = 0

for i in range(len(input_2_1_list)):

    if int(input_2_1_list[i]) + int(input_2_2_list[i]) >= 10:

        carry += 1

if carry ==  0:
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")

###############################################

input_3_1_list = list(input_3_1)                                        # 세번째 input
input_3_2_list = list(input_3_2)

if len(input_3_1_list) > len(input_3_2_list):
    for i in range(len(input_3_1_list) - len(input_3_2_list)):
        input_3_2_list.insert(0,"0")

elif len(input_3_1_list) < len(input_3_2_list):
    for i in range(len(input_3_2_list) - len(input_3_1_list)):
        input_3_1_list.insert(0,"0")

carry = 0

for i in range(len(input_3_1_list)):

    if int(input_3_1_list[i]) + int(input_3_2_list[i]) >= 10:

        carry += 1

if carry ==  0:
    print("NO carry operation")

else:
    print(f"{carry} carry opperation")