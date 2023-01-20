#========================================================================
#여기서의 “부분”은 LCS문제에서의 “부분”과는 다른 의미임을 명심하라. nice라는 문자열이 있다면 이 문제에서의 부분문자열의 집합은 {‘’, n, i, c, e, ni, ic, ce, nic, nice}이다.
#LCS문제에서의 “부분”에서는 nce도 하나의 부분문자열로 볼 수 있지만 이 문제에서는 부분문자열이 아니다. (즉, 이 문제에서의 “부분”은 원래 문자열에서 일정 부분을 잘라낸 것이다.)
#photography와 autograph 두 문자열이 있다고 할 때, ph, grap, to 등의 부분문자열이 있으며, 이 중 최대의 길이를 갖는 부분문자열은 tograph이다.

#입력
#두 줄에 각각의 스트링이 주어진다. 각 스트링의 길이는 4000이하이다.
#photography
#autograph

#출력
#첫줄에 찾은 부분문자열의 길이, 둘째 줄에 가장 긴 공통의 부분문자열을 출력한다.
#7
#tograph
#========================================================================
#과제1. 입력된 문자열의 부분문자열을 구하시오. 
#      - 조건1. 부분문자열은 입력된 문자열 안에 연속된 문자열을 의미한다.
#      - 조건2. 부분문자열에는 공집합도 포함
#      - input_string = 'nice'
#      - 출력값 = ['','n','i','c','e','ni','ic','ce','nic','ice','nice']

#과제 1 풀이
result = []                                  #result 명의 빈 리스트 생성
input_str = input('string = ')               #input_str에 값 저장
for i in range(len(input_str)):              #for문을 이용하여 i를 input_str의 길이만큼 반복
      for j in range(i, len(input_str) + 1): #for문을 이용해여 j를 i부터 input_str의 길이 + 1까지 반복
            result.append(input_str[i:j])    #result에 input_str의 i번째부터 j번째까지 리스트에 추가
print(list(set(result)))                     #중복을 제거한 result 리스트 출력
#========================================================================
#과제2. 아래와 같이 두 문자열이 입력되었을 때, 두 문자열의 공통된 부분문자열 중 가장 긴 부분문자열의 길이와 실제값을 출력하시오.
#      - 조건1. 부분문자열은 입력된 문자열 안에 연속된 문자열을 의미한다.
#      - 조건2. 부분문자열에는 공집합도 포함
#      - input_string1 = 'photography'
#      - input_string2 = 'autograph'
#      - 출력값 = 7 tograph

#과제 2 풀이
def stringpart_(str_):                      #def로 문자열을 값으로 받는 stringpart_ 함수 생성
    return set(str_[i:j] for i in range(len(str_)) for j in range(i, len(str_) + 1)) #슬라이스한 값을 중복 제거한 집합으로 반환

str_1 = input('string1 = ')                                      #input_string1 입력
str_2 = input('string2 = ')                                      #input_string2 입력
result = max(stringpart_(str_1) & stringpart_(str_2), key = len) #str_1과 str_2의 교집합을 구한 뒤 문자열 길이가 가장 큰 값을 반환하여 result에 저장
print(len(result), result)                                       #result의 길이와 result 출력
#========================================================================
