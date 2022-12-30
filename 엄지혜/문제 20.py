#-----------------  Question  -----------------
#지뢰찾기 게임은 M x N 매트릭스에 위치해 있는 지뢰를 찾는 게임이다.
#M x N 매트릭스 상의 격자(square)는 지뢰이거나 지뢰가 아니다.
#지뢰 격자는 *로 표시한다. 지뢰가 아닌 격자(square)는 숫자로 표시하며 그 숫자는 인접해 있는 지뢰의 수를 의미한다.
#(격자(sqaure)는 최대 8개의 인접한 지뢰를 가질 수 있다.)
#다음은 4x4 매트릭스에서 2개의 지뢰(*)를 표시하는 방법이다.
# *...
# ....
# .*..
# ....
#이 게임의 목표는 지뢰의 위치(*)를 제외한 나머지 격자들의 숫자를 맞추는 것이다.
#위 경우의 답은 아래와 같다.
# *100
# 2210
# 1*10
# 1110
#입력 : 첫번째 줄은 M x N 의 M(행)과 N(열)에 해당되는 숫자이다.
#       N과 M은 0보다 크고 100 이하이다(0< N, M <=100).
#       그 다음 M개의 줄이 차례로 입력되고 각 줄은 정확하게 N개의 문자가 입력된다.
#       지뢰 격자는 *로 표시하며 지뢰가 아닌 격자는 .(dot)로 표시한다.
#출력 : 지뢰(*)를 제외한 나머지 격자의 숫자값을 찾아서 M x N 매트릭스를 출력한다.
#----------------------------------------------
#과제 1. input의 숫자만큼 '*'과 '.'으로 구성된 문자열을 출력하시오. 
#      - 조건1 : random 모듈을 활용하시오.
#      - input = '4'
#      - 출력 : *.** 또는 ...* 등등

#과제 1 풀이
import random                                     #random 모듈 사용
m = int(input("input = "))                        #m에 input을 이용해 외부값을 받고 이를 숫자로 변환하여 저장
n = m                                             #n에 m값 저장

mn = [[random.choice(['.','.','.','.','*']) for x in range(n)] for y in range(m)] #mn에 random으로 
for y in mn:                                      #
    print(''.join(y))                             #
r = mn.copy()                                     #
for y, yd in enumerate(r):
    for x, xd in enumerate(yd):
        if r[y][x] == '*': continue
        count = 0
        c = [[''] if y - 1 < 0 else r[y-1][0 if x - 1 < 0 else x - 1:x+2],
             r[y][0 if x - 1 < 0 else x - 1:x+2],             
             [''] if y + 1 >= m else r[y+1][0 if x - 1 < 0 else x - 1:x+2]]
        for z in c:
            count+=z.count('*')
        r[y][x] = str(count)

#----------------------------------------------
#과제 2. 행과 열을 입력하면 '*'과 '.'으로 구성된 행렬을 출력하시오.
#      - 조건1 : random 모듈을 활용하시오.
#      - 조건2 : 행과 열은 1보다 크고 100 이하인 정수이다.
#      - row = 3
#      - column = 6
#      - 출력 (예시이며 random 모듈을 사용하였으므로 결과는 다를 수 있음.)
#        [['*', '.', '.', '.', '*', '.'], 
#        ['.', '.', '*', '.', '.', '.'],
#        ['.', '.', '.', '*', '.', '*']]

#과제 2 풀이
import random
m = int(input("M:"))
n = int(input("N:"))
if not(n > 0 and m <= 100):
    raise Exception("N > 0, M <= 100")
mn = [[random.choice(['.','.','.','.','*']) for x in range(n)] for y in range(m)]
for y in mn:
    print(''.join(y))
r = mn.copy()
for y, yd in enumerate(r):
    for x, xd in enumerate(yd):
        if r[y][x] == '*': continue
        count = 0
        c = [[''] if y - 1 < 0 else r[y-1][0 if x - 1 < 0 else x - 1:x+2],
             r[y][0 if x - 1 < 0 else x - 1:x+2],             
             [''] if y + 1 >= m else r[y+1][0 if x - 1 < 0 else x - 1:x+2]]
        for z in c:
            count+=z.count('*')
        r[y][x] = str(count)

#----------------------------------------------
#과제 3. 과제2에서 생성한 행렬을 이용하여 지뢰(*)를 제외한 나머지 격자의 숫자값을 찾고 행렬을 출력하시오.
#      - 조건1 : random 모듈을 활용하시오.
#      - 조건2 : 행과 열은 1보다 크고 100 이하인 정수이다.
#      - row = 3
#      - column = 6
#      - 출력 (예시이며 random 모듈을 사용하였으므로 결과는 다를 수 있음.)
#        *212*1
#        12*332
#        012*2*

#과제 3 풀이
import random
m = int(input("M:"))
n = int(input("N:"))
if not(n > 0 and m <= 100):
    raise Exception("N > 0, M <= 100")
mn = [[random.choice(['.','.','.','.','*']) for x in range(n)] for y in range(m)]

r = mn.copy()
for y, yd in enumerate(r):
    for x, xd in enumerate(yd):
        if r[y][x] == '*': continue
        count = 0
        c = [[''] if y - 1 < 0 else r[y-1][0 if x - 1 < 0 else x - 1:x+2],
             r[y][0 if x - 1 < 0 else x - 1:x+2],             
             [''] if y + 1 >= m else r[y+1][0 if x - 1 < 0 else x - 1:x+2]]
        for z in c:
            count+=z.count('*')
        r[y][x] = str(count)

print("output")
for y in r:
    print(''.join(y)) 

#----------------------------------------------
