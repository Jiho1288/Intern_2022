#---------------------------------------------------------------------------------
# - 첫 번째 계산
#   아이들은 여러 자리 숫자들을 더하기 위해서 우에서 좌로 숫자를 하나씩 차례대로 더 하라고 배웠다.
#   1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는 "한자리올림"연산을 많이 발견하는 것은 중요한 도전이 된다.
#   당신의 일은 교육자가 그들의 어려움을 평가하기 위하여, 덧셈 문제들의 각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.
# - 입력
#   입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다.
#   입력의 마지막 라인은 0 0 을 포한한다.
# - 출력
#   마지막을 제외한 입력의 각 라인에 대해서 당신은 두 숫자들을 더한 결과에서 한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.
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
b = []                                  # b에 빈 리스트 생성
while True:                             # while문을 통해 반복문 생성
  cnt=0
  A, B = input("Input = ").split(' ')   # A와 B에 input을 이용해 외부입력값을 받아 저장
  if A=='0' and B=='0':                 # ==를 통해 A와 B가 0와 같다면
    break                               # break 문을 통해 중지
  else:                                 # A와 B 둘 중 0이 아닌 경우가 있다면
    for i in range(len(A)):             # for문을 A의 길이만큼 반복
      if int(A[i])+int(B[i])>=10:       # A와 B를 숫자로 변환하여 합이 10보다 크거나 같으면 
        cnt+=1                          # cnt에 1을 더해 할당
    if cnt==0:                          # if문을 사용해 c가 0이라면
      b.append('No carry operation')    # b에 'No carry operation' 추가로 저장
    else:                               # else문을 사용해 c가 0이 아니라면
      b.append(str(cnt) +' carry operation')   # b에 cnt를 문자열로 변환하고 'carry operation'을 더해 저장
print(*b, sep='\n')                            # 출력

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
b = []                                  # b에 빈 리스트 생성
while True:                             # while문을 통해 반복문 생성
  cnt=0
  A, B = input("Input = ").split(' ')   # A와 B에 input을 이용해 외부입력값을 받아 저장
  if A=='0' and B=='0':                 # ==를 통해 A와 B가 0와 같다면
    break                               # break 문을 통해 중지
  
  else:                                 # A와 B 둘 중 0이 아닌 경우가 있다면
    if len(A) > len(B):                 # A의 길이가 B의 길이보다 길다면
      A_B = len(A) - len(B)             # A_B에 A의 길이와 B의 길이를 빼서 할당
      for j in range(A_B):              # for문을 이용해 71의 결과값만큼 반복
        B = '0' + B                     # B에 '0'에 B를 더해 저장
      for i in range(len(A)):           # for문을 이용해 A의 길이만큼 반복
        if int(A[i])+int(B[i])>=10:     # A와 B를 숫자로 변환하여 합이 10보다 크거나 같으면 
          cnt+=1                        # cnt에 1을 더해 할당
      if cnt==0:                        # if문을 사용해 c가 0이라면
        b.append('No carry operation')  # b에 'No carry operation' 추가로 저장
      else:                             # else문을 사용해 c가 0이 아니라면
        b.append(str(cnt) +' carry operation') # b에 cnt를 문자열로 변환하고 'carry operation'을 더해 저장
    
    else:                               # A의 길이가 B의 길이보다 작다면
      B_A = len(B) - len(A)             # A_B에 A의 길이와 B의 길이를 빼서 할당
      for h in range(B_A):              # for문을 이용해 83의 결과값만큼 반복
        A = '0' + A                     # A에 '0'에 A를 더해 저장
      for i in range(len(A)):           # for문을 이용해 A의 길이만큼 반복
        if int(A[i])+int(B[i])>=10:     # A와 B를 숫자로 변환하여 합이 10보다 크거나 같으면
          cnt+=1                        # cnt에 1을 더해 할당
      if cnt==0:                        # if문을 사용해 c가 0이라면
        b.append('No carry operation')  # b에 'No carry operation' 추가로 저장
      else:                             # else문을 사용해 c가 0이 아니라면
        b.append(str(cnt) +' carry operation')  # b에 cnt를 문자열로 변환하고 'carry operation'을 더해 저장
              
print(*b, sep='\n')  # 결과 PRINT

#---------------------------------------------------------------------------------
