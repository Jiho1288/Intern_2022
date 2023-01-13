"""
두 날짜(YYYYMMDD)의 차이 일수를 구하는 프로그램을 작성하시오.

※ 단, 프로그래밍 언어에서 지원하는 날짜차이를 계산하는 라이브러리는 사용하지 말것

예)

20070515 sub 20070501 = 14
20070501 sub 20070515 = 14
20070301 sub 20070515 = 75
"""
"""
========================================================================
과제1. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
      - first = 20070501
      - second = 20070515
      - 출력값 : 14
========================================================================
"""

def q1():
    date = input('first=')                      # 변수 date에 input을 받음
    year = int(date[0:4])                       # 0번째부터 4번째까지 슬라이싱하여 년도를 받아옴
    month = int(date[4:6])                      # 같은 방식으로 달과
    day = int(date[6:8])                        # 일을 받아옴
    month_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 달의 일정보를 month_1st에 저장

    year_1 = (year-1)*365 + (year//4)           # 년도에서 1을 뺀 후 365를 곱해주고 윤년을 계산해줌
    month_1 = 0

    for i in range(month-1):                    # for문 이용
        month_1 = month_1 + month_lst[i]        # 달의 일정보를 month_1에 계속 저장
        
    if year%4==0 and month>2:                   # 그리고 윤년 2월 이후에 태어난 사람에게는 1을 더해주어
        month_1 = month_1 + 1                   # month_1에 저장

    day_1 = year_1 + month_1 + day              # 년,달,일수를 계산해서 day_1에 저장

    #---------------------------------------------------------------------------------

    date = input('second=')                     # day_2도 동일한 방식으로 계산하고
    year = int(date[0:4])                       # day1에서 day2 절대값 해준다
    month = int(date[4:6])
    day = int(date[6:8])
    month_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year_1 = (year-1)*365 + (year//4)
    month_1 = 0

    for i in range(month-1):
        month_1 = month_1 + month_lst[i]
        
    if year%4==0 and month<2:
        month_1 = month_1 - 1

    day_2 = year_1 + month_1 + day

    print(abs(day_1-day_2))

"""
========================================================================
과제2. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
      - first = 20070301
      - second = 20070515
      - 출력값 : 75
========================================================================
"""

def q2():
    date = input('first=')                      #과제2도 과제1과 동일
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    month_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year_1 = (year-1)*365 + (year//4)
    month_1 = 0

    for i in range(month-1):
        month_1 = month_1 + month_lst[i]
        
    if year%4==0 and month>2:
        month_1 = month_1 + 1

    day_1 = year_1 + month_1 + day

    date = input('second=')
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    month_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year_1 = (year-1)*365 + (year//4)
    month_1 = 0

    for i in range(month-1):
        month_1 = month_1 + month_lst[i]
        
    if year%4==0 and month<2:
        month_1 = month_1 - 1

    day_2 = year_1 + month_1 + day

    print(abs(day_1-day_2))



if __name__ == "__main__":
    q1()
    q2()