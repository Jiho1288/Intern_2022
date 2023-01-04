"""
2나 5로 나누어 떨어지지 않는 1 이상 10,000 이하의 정수 n이 주어졌는데, n의 배수 중에는 10진수로 표기했을 때 모든 자리 숫자가 1인 것이 있다.
그러한 n의 배수 중에서 가장 작은 것은 몇 자리 수일까?

Sample Input
3
7
9901

Sample Output
3
6
12
"""

"""
=============================================================================
과제 1. 2나 5로 나누어 떨어지지 않는 1 이상 10,000 이하의 정수는 모두 몇 개인지 구하시오
       - output : 4000
=============================================================================

"""
print('****과제1****')

num_list = []                  # num_list에 빈 리스트 생성
for i in range(1,10001):       # for를 사용하여 i를 1부터 10000까지 반복
    if i%2!=0 and i%5!=0:      # i를 2로 나눴을때 나머지가 0이 아니고,5로 나눴을때 나머지가 0이 아닐때
        num_list.append(i)     # num_list에 i를 추가
print(len(num_list))           # num_list의 요소 개수 출력

"""
=============================================================================
과제 2. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수와 그 수의 자리수를 구하시오
       - input =  7
       - output = 111111 6
=============================================================================
"""
print('****과제2****')

num = int(input('input:'))                 # num변수에 input값 저장
a = 0                                      # 반복문이 실행될 때마다 num값을 더해서 배수를 구하기위해 a값 초기화

while True:                                # while 무한루프 실행
    a = a+num                              # a값에 num값을 계속 더해서 배수 생성
    a_list = list(str(a))                  # 정수형a를 list로 변경 후 a_list에 저장
    result = 0                             # 각 자릿값을 더하기 위해 result변수 초기화
    for i in range(len(a_list)):           # a의 첫자리에서 끝자리까지 반복문을 통해 
        if int(a_list[i])==1:              # 그 자릿값이 1일때 
            result=result+int(a_list[i])   # result변수에 더해줌
    if len(str(a))==result:                # 만약 전체 자릿값과 result값이 같다면
        print(a,len(str(a)))               # a와 a의 자릿값 출력후
        break                              # 반복문 탈출
    
"""
=============================================================================
과제 3. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수의 자리수를 구하시오
       - input =  3, 7, 9901
       - output = 3, 6, 12
=============================================================================
"""
print('****과제3****')                     

num_input=input('input:')                  
num_list=num_input.split(' ')              # input값을 split함수로 분해 후 num_list에 저장
output_list=[]                             # 출력을 저장할 빈 리스트 생성 
for i in range(len(num_list)):             # num_list의 각 요소에 차례대로 접근
    num = int(num_list[i])                 # 나머지는 과제2와 동일
    a= 0
    while True:
        a = a+num
        a_list = list(str(a)) #자릿값구하긩
        result = 0
        for i in range(len(a_list)):
            if int(a_list[i])==1:
                result=result+int(a_list[i])
        if len(str(a))==result:
            break
        
print(*output_list)