"""
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
n을 d(n)의 제네레이터(generator)라고 한다.
예를 들어 d(91) = 9 + 1 + 91 = 101인 경우 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.

예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
"""

"""
==========================================================================
# 과제 1. 1부터 30까지의 자연수 중에서, 제너레이터가 있는 수의 합을 구하시오. 
## 출력 : 420
==========================================================================
"""

print("***과제1***")

natural_list = []                           # 빈 list를 생성하여 natural_list 변수에 저장

for i in range (1,31):                      # natural_list에 1부터 30까지 자연수 추가
    natural_list.append(i)

generator_set = set()                       # generator를 저장할 빈 set 자료형 생성 (중복을 피하기 위해 set 자료형 사용)

for n in natural_list:                      # 반복문을 통해 natural list의 각 요소에 접근

    place_value = list(str(n))              # 각 자연수를 string type으로 변환후 list로 place_value(자릿수) 변수에 저장 

    generator = n                           # generator 변수 생성 후 자연수 n 저장

    for j in range (len(place_value)):      # 반복문을 활용하여 위의 place_value(자릿수)를 generator에 더해준다

        generator += int(place_value[j])
    
    if generator in natural_list:           # if 문을 활용하여 generator가 natural list 범위 내에 있다면 generator_set에 추가
        generator_set.add(generator)

print(sum(generator_set))                   # generator들의 합을 출력         

"""
==========================================================================
# 과제 2. 1이상 5000 미만의 셀프 넘버(제너레이터가 하나도 없는 수)의 합을 구하시오.
## 출력 : 1227365
==========================================================================
"""

print("\n***과제2***")

natural_list = []

for i in range (1,5001):
    natural_list.append(i)

generator_set = set()

for n in natural_list:
    place_value = list(str(n))

    generator = n

    for j in range (len(place_value)):

        generator += int(place_value[j])
    
    if generator in natural_list:
        generator_set.add(generator)

sum_natural = sum(natural_list)             # 모든 자연수의 합

sum_generator = sum(generator_set)          # generator의 합

print(sum_natural-sum_generator)            # Self Number (모든 자연수 - 제네레이터) 출력


# reference: https://m31phy.tistory.com/176
# 리스트 내에 element가 존재하는지 확인
