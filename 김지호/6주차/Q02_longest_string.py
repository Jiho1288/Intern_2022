'''
여기서의 “부분”은 LCS문제에서의 “부분”과는 다른 의미임을 명심하라. nice라는 문자열이 있다면 이 문제에서의 부분문자열의 집합은 {‘’, n, i, c, e, ni, ic, ce, nic, nice}이다.

LCS문제에서의 “부분”에서는 nce도 하나의 부분문자열로 볼 수 있지만 이 문제에서는 부분문자열이 아니다. (즉, 이 문제에서의 “부분”은 원래 문자열에서 일정 부분을 잘라낸 것이다.)

photography와 autograph 두 문자열이 있다고 할 때, ph, grap, to 등의 부분문자열이 있으며, 이 중 최대의 길이를 갖는 부분문자열은 tograph이다.

입력

두 줄에 각각의 스트링이 주어진다. 각 스트링의 길이는 4000이하이다.

photography
autograph
출력

첫줄에 찾은 부분문자열의 길이, 둘째 줄에 가장 긴 공통의 부분문자열을 출력한다.

7
tograph

'''
"""
========================================================================
과제1. 입력된 문자열의 부분문자열을 구하시오. 
      - 조건1. 부분문자열은 입력된 문자열 안에 연속된 문자열을 의미한다.
      - 조건2. 부분문자열에는 공집합도 포함
      - input_string = 'nice'
      - 출력값 = ['','n','i','c','e','ni','ic','ce','nic','ice','nice']
========================================================================
"""

def q1():
    a = input('input_string = ')            # input 값을 변수 a에 저장
    subset = set()                          # 문자열 변수 a의 부분집합을 저장할 빈 set 생성

    for i in range(len(a)):                 # 문자의 길이만큼 for문을 반복하고
        for j in range(i,len(a)+1):         # 다중 for문을 사용하여 i 부터 문자의 마지막 자리까지 반복 
            subset.add(a[i:j])              # 문자의 i번째 부터 j번째까지 slicing 하여 subset에 저장

    print(subset)                           # 결과값 subset를 출력

"""
========================================================================
과제2. 아래와 같이 두 문자열이 입력되었을 때, 두 문자열의 공통된 부분문자열 중 가장 긴 부분문자열의 길이와 실제값을 출력하시오.
      - 조건1. 부분문자열은 입력된 문자열 안에 연속된 문자열을 의미한다.
      - 조건2. 부분문자열에는 공집합도 포함
      - input_string1 = 'photography'
      - input_string2 = 'autograph'
      - 출력값 = 7 tograph
========================================================================
"""

def q2():
    a = input('input_string1 = ')           # input을 두개 받아준 후
    b = input('input_string2 = ')
    subset_a = set()                        # 문자열 변수 a,b의 부분집합들을 저장할 빈 set 두개 성성
    subset_b = set()

    for i in range(len(a)):                 # 과제1과 동일하게 a와 b의 부분집합을 구해줌
        for j in range(i,len(a)+1):
            subset_a.add(a[i:j])

    for i in range(len(b)):
        for j in range(i,len(b)+1):
            subset_b.add(b[i:j])

    c = subset_a & subset_b                 # 두 부분집합의 교집합을 c에 저장

    max_str = max(c, key=len)               # max함수에서 key를 len으로 설정하여 c에서 가장 긴 문자를 max_str에 저장

    print(len(max_str), max_str)            # 결과값 출력



if __name__ == '__main__':
      print('=====과제1=====')
      q1()
      print('=====과제2=====')
      q2()