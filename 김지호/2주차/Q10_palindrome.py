"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 한다.
- 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99)이다.
- 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하여라.
"""

"""
==========================================================================
# 과제 1. 세 자리 수를 곱해서 만들들 수 있는 가장 큰 대칭수를 구하시오.
## 출력 : 906609
==========================================================================
"""

print("***과제1***")

multiply_list = []                      # 세자리 수 곱셈 결과를 저장하기 위한 빈 List 생성

for i in range (100,1000):              # 다중 반복문을 이용하여 100부터 999까지 모든 곱셈 실행
    for j in range (100,1000):
        result = i*j
        multiply_list.append(result)

multiply_list.sort(reverse=True)        # 이를 내림 차순 정리

for i in multiply_list:                 # 곱셈이 저장되어 있는 리스트에 반복문을 활용 하여 대칭수를 찾은 후에 break
    str_multiply = str(i)

    if str_multiply[0]==str_multiply[5] and str_multiply[1]==str_multiply[4] and str_multiply[2]==str_multiply[3]:
        print(str_multiply)             # 이때 곱셈결과를 string으로 변환 후 if 문을 활용하여 각 자릿수가 대칭인지 확인후 출력 및 for문 중지
        break

"""
==========================================================================
# 과제 2. 출력 값에 천자리 구분기호가 나오도록 변환해 보세요(format()함수 사용)
## 출력 : 906,609
==========================================================================
"""

print("\n***과제2***")

multiply_list = []

for i in range (100,1000):
    for j in range (10,1000):
        result = i*j
        multiply_list.append(result)

multiply_list.sort(reverse=True)

for i in multiply_list:
    str_multiply = str(i)

    if str_multiply[0]==str_multiply[5] and str_multiply[1]==str_multiply[4] and str_multiply[2]==str_multiply[3]:
        print("{0}{1}{2},{3}{4}{5} " .format(str_multiply[0], str_multiply[1], str_multiply[2], str_multiply[3], str_multiply[4], str_multiply[5] ))
        break                           # format 함수를 활용하여 자릿수를 각각 출력해주고 가운데에 콤마 추가