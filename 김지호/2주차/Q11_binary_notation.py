"""
2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다.
예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에 1001001으로 표현한다.
어떤 숫자를 입력받았을 때 그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.
"""

"""
==========================================================================
# 과제 1. input()함수를 사용하고, input값을 이진법으로 나타내시오.
## input = 73
## 출력 : 1001001
==========================================================================
"""
print("***과제1***")

str_decimal = input("input=")       # 10진수 값을 입력받고 str_decimal 변수에 저장

decimal = int(str_decimal)          # 입력값을 integer 값으로 변경

binary = ""                         # 이진수 결과 값에 대한 빈 string 생성

power_2 = 1

exponent = 0                        

while True:                         # 2진수의 자릿수를 알아내기 위해 while 무한루프로 2를 계속 제곱 시켜주고

    exponent += 1                   # 제곱시켜준 값이 입력된 수보다 커지면 break 

    power_2 *= 2

    if decimal < power_2:
        break 

power_n = exponent - 1              # 이때 지수-1 값 을 power_n 에 저장 (입력된 값보다 제곱시켜준 값이 작아야하므로)

for i in range(power_n,-1,-1):      # 몫과 나머지를 이용하여 2의 n 제곱부터 2의 0제곱까지 반복문을 통한 2진수 계산

    quotient = int(decimal)//(2**i)
        
    binary += str(quotient)         # 몫은 차례대로 string 으로 변경 후 binary 변수에 저장

    decimal = int(decimal) % 2**i   # 나머지는 decimal 변수에 초기화 후 반복문 지속

print(binary)


"""
==========================================================================
# 과제 2. input()함수를 사용하고, input값을 16진법으로 나타내시오.
## input = 173
## 출력 : AD
==========================================================================
"""

print("\n***과제2***")

str_decimal = input("input=")

decimal = int(str_decimal)

hexadecimal = ""

power_16 = 1

exponent = 0

while True:
    
    exponent += 1

    power_16 *= 16                      # 16으로 제곱되는 값을 변경

    if decimal < power_16:
        break 

power_n = exponent - 1

for i in range(power_n,-1,-1):           

    quotient = decimal//(16**i)         # if 문을 통해 몫이 10부터 15일 때 결과를 A부터 E로 변경
        
    str_quotient = str(quotient)    

    if quotient == 10:
        str_quotient = "A"

    if quotient == 11:
        str_quotient = "B"

    if quotient == 12:
        str_quotient = "C"

    if quotient == 13:
        str_quotient = "D"

    if quotient == 14:
        str_quotient = "E"

    if quotient == 15:
        str_quotient = "F"

    hexadecimal += str_quotient

    decimal = decimal % 16**i


print(hexadecimal)