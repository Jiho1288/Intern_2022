#========================================================================
#두 날짜(YYYYMMDD)의 차이 일수를 구하는 프로그램을 작성하시오.
#※ 단, 프로그래밍 언어에서 지원하는 날짜차이를 계산하는 라이브러리는 사용하지 말것
#예)
#20070515 sub 20070501 = 14
#20070501 sub 20070515 = 14
#20070301 sub 20070515 = 75
#========================================================================
#과제1. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
#      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
#      - first = 20070501
#      - second = 20070515
#      - 출력값 : 14

#========================================================================
#과제2. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
#      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
#      - first = 20070301
#      - second = 20070515
#      - 출력값 : 75
#========================================================================
#과제 1,2 풀이
F = int(input('first = '))                #F에 input로 first 값을 받고 int를 통해 정수로 변환 후 저장 
S = int(input('second = '))               #S에 input로 second 값을 받고 int를 통해 정수로 변환 후 저장 
F_year = (F // 10000) % 10000             #F_year에 F를 10,000으로 나눈 몫을 10,000으로 나눈 나머지 저장
S_year = (S // 10000) % 10000             #S_year에 S를 10,000으로 나눈 몫을 10,000으로 나눈 나머지 저장
F_mouth = (F // 100) % 100                #F_mouth에 F를 100으로 나눈 몫을 100으로 나눈 나머지 저장
S_mouth = (S // 100) % 100                #S_year에 S를 100으로 나눈 몫을 100으로 나눈 나머지 저장
F_data = F % 100                          #F_data에 F를 100으로 나눈 나머지 저장
S_data = S % 100                          #S_data에 S를 100으로 나눈 나머지 저장
d_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #d_list에 리스트 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 저장
min_F_year = (F_year - 1) * 365           #min_F_year에 (F_year - 1) * 365 값 저장
min_S_year = (S_year - 1) * 365           #min_S_year에 (S_year - 1) * 365 값 저장
min_F_mouth = sum(d_list[:F_mouth - 1])   #min_F_mouth에 d_list의 0번째부터 F_mouth - 1까지 더해 저장 
min_S_mouth = sum(d_list[:S_mouth - 1])   #min_S_mouth에 d_list의 0번째부터 S_mouth - 1까지 더해 저장 
min_F_data = F_data - 1                   #min_F_data에 F_data - 1 값 저장   
min_S_data = S_data - 1                   #min_S_data에 S_data - 1 값 저장
F_year_2 = int(F_year / 4) - int(F_year / 100) + int(F_year / 400)  #F_year_에 [(F_year / 4) - (F_year / 100) + (F_year / 400)] 저장
S_year_2 = int(S_year / 4) - int(S_year / 100) + int(S_year / 400)  #S_year_2에 [(S_year / 4) - (S_year / 100) + (S_year / 400)] 저장
F1 = (min_F_year + min_F_mouth + min_F_data + F_year_2)             #F1에 (min_F_year + min_F_mouth + min_F_data + F_year_2) 값 저장
S2 = (min_S_year + min_S_mouth + min_S_data + S_year_2)             #S2에 (min_S_year + min_S_mouth + min_S_data + S_year_2) 값 저장

# 과제 1,2 출력
print(int(((S2 - F1) ** 2) ** (1 / 2)))   # 절대값 비슷
#========================================================================
