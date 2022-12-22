#---------------------------------------------------------------------------------
# - 첫 번째 계산
#   아이들은 여러 자리 숫자들을 더하기 위해서
#   우에서 좌로 숫자를 하나씩 차례대로 더 하라고 배웠다.
#   1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는 "한자리올림"연산을
#   많이 발견하는 것은 중요한 도전이 된다.
#   당신의 일은 교육자가 그들의 어려움을 평가하기 위하여,
#   덧셈 문제들의 각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.
# - 입력
#   입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다.
#   입력의 마지막 라인은 0 0 을 포한한다.
# - 출력
#   마지막을 제외한 입력의 각 라인에 대해서 당신은 두 숫자들을 더한 결과에서
#   한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.
# [입력 샘플]
# 123 456
# 555 555
# 123 594
# 0 0
# [출력 샘플]
# No carry operation
# 3 carry operation
# 1 carry operation
#---------------------------------------------------------------------------------
# 과제 1. 입력 값의 자릿수가 같을 때 한자리 올림 계산 횟수를 출력하시오.
## Input :  123 456
#           555 555
#           123 594
#           0 0
## 출력 :   No carry operation
#          3 carry operation
#          1 carry operation
## 조건 1> 입력이 총 4번 완료된 후에 계산이 수행되도록 하세요.
## 조건 2> 입력값은 '123 456'의 형태로 받습니다.

# 과제 1 풀이
def count(numbers):
    num_list= numbers.split(" ")
    num1=num_list[0]
    num2=num_list[1]

    #0을 채워 두 수의 길이를 맞춤.
    while len(num1)!=len(num2):
        if len(num1)>len(num2):
            num2='0'+num2
        else:
            num1='0'+num1

    count=0 #올린 횟수
    tenup=0 #올림될 경우 1, 아닐경우 0
    for i in range(1,max([len(num1)+1,len(num2)+1])):

        sum=0
        if int(num1[-i])+int(num2[-i])+tenup<10:
            sum+=int(num1[-i])+int(num2[-i])
            tenup=0
        else:
            sum+=int(num1[-i])+int(num2[-i])+tenup-10
            count+=1
            tenup=1
    return count

nums=''
resert=[]
while nums != '0 0':#0 0이 입력될 때 까지 계속 입력
    nums=input()
    if nums !='0 0': #0 0인 경우 출력x
        pass
        if count!=0:
            resert.append('%d carry operation.'%count(nums))
        else:
            resert.append('No carry operation.')
    else:
        pass
print('\n'.join(resert))

#---------------------------------------------------------------------------------
# 과제 2. 입력 값의 자릿수가 다를 때의 한자리 올림 계산 횟수를 출력하시오.
## Input : 13 452
#          55 555
#          1009 99
#          0 0
## 출력 : No carry operation
#        2 carry operation
#        1 carry operation
## 조건 1> 입력이 총 4번 완료된 후에 계산이 수행되도록 하세요.
## 조건 2> 입력값은 '13 452'의 형태로 받습니다.

#과제 2 풀이



#---------------------------------------------------------------------------------
