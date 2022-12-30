#---------------------  Question  ---------------------
#어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다.
#이렇게 해서 새로 만들어진 숫자를 n으로 놓고, n=1 이 될때까지 같은 작업을 계속 반복한다.
#예를 들어, n=22이면 다음과 같은 수열이 만들어진다.
#- 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#n이라는 값이 입력되었을때 1이 나올때까지 만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다.
#위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다.
#i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.
#------------------------------------------------------
#과제 1. 입력 값(n)이 40일때, 사이클 길이를 구하시오.
#       - input = 40
#       - 출력 : 9

# 과제 1 풀이 
def cyclelen(n) :                       # def함수를 이용해 함수 cyclelen에 n이라는 숫자가 주어진다면
    n = [n]                             # n을 리스트에 넣어줌
    while(n[-1]!=1) :                   # while문을 이용해 n이 1이 아닐때까지 반복  # n[-1] 리스트 중 가장 마지막에 나온 것 
        if n[-1] % 2 == 0 :             # if 문을 사용하여 n[-1]를 2로 나누어 0이라면 즉, 짝수라면,
            n.append(n[-1]//2)          # 2를 나눈 후, append에 n에 추가하여 저장
        else:                           # n[-1]를 2로 나누어 0이 아니라면 즉, 홀수라면,
            n.append(n[-1] * 3 + 1)     # 3을 곱하고 1을 더한 후, append에 n에 추가하여 저장
    return len(n)                       # n의 길이를 구해 반환

print(cyclelen(int(input('input = ')))) # cyclelen에 input을 통해 외부값을 받고 이를 숫자로 변환하여 저장을 프린트

#------------------------------------------------------
#과제 2. i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수에 대한 최대 사이클 길이(i와 j도 사이클 길이에 포함됨)를 구하라.
#       - start = 1
#       - end = 10
#       - 출력 : 20

#과제 2 풀이 
cmd_i = int(input("start = "))                 #input을 통해 외부값을 받고 이를 숫자로 변환하여 i에 저장
cmd_j = int(input("end = "))                   #input을 통해 외부값을 받고 이를 숫자로 변환하여 j에 저장

num_range = range(cmd_i, cmd_j + 1)            #범위를 지정하는 range를 이용해 i부터 j까지의 값을 num_range에 저장

cycle_list = []                                #cycle_list 명의 리스트 생성

for n in num_range:                            #for문을 이용해 반복
    num_list = []                              #num_list 명의 리스트 생성
    while n != 1:                              #while문을 이용해 반복
        num_list.append(n)                     #num_list에 append를 통해 n을 추가 
 
        if n % 2 == 0:                         #if를 이용해 n%2가 0이라면
            num = n/2                          #num는 n을 2로 나눈 값
            n = num                            #n은 num

        else:                                  #if를 이용해 n%2가 0이 아니라면
            num = n*3 +1                       #num는 n*3 +1의 값
            n = num                            #n는 num

    cycle_list.append(len(num_list)+1)         #cycle_list에 append를 이용해 num_list의 길이에 1을 더해 저장

print(f"{max(cycle_list)}")                    #결과값 프린트

#------------------------------------------------------
#과제 3. i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수에 대한 최대 사이클 길이(i와 j도 사이클 길이에 포함됨)를 구하라.
#       - start_num_list = [1, 100, 201, 900]
#       - end_num_list = [10, 200, 210, 1000] 
#       - 출력 : [20, 125, 89, 174]

#과제 3 풀이
def cyclelen(n) :                       # def함수를 이용해 함수 cyclelen에 n이라는 숫자가 주어진다면
    n = [n]                             # n을 리스트에 넣어줌
    while(n[-1]!=1) :                   # while문을 이용해 n이 1이 아닐때까지 반복  # n[-1] 리스트 중 가장 마지막에 나온 것 
        if n[-1] % 2 == 0 :             # if 문을 사용하여 n[-1]를 2로 나누어 0이라면 즉, 짝수라면,
            n.append(n[-1]//2)          # 2를 나눈 후, append에 n에 추가하여 저장
        else:                           # n[-1]를 2로 나누어 0이 아니라면 즉, 홀수라면,
            n.append(n[-1] * 3 + 1)     # 3을 곱하고 1을 더한 후, append에 n에 추가하여 저장
    return len(n)                       # n의 길이를 구해 반환

i = list(map(int, input('start = ').split(",")))   #i에 input를 이용해 외부값을 받아 값 중간에 ,를 찍고 숫자로 변환하여 리스트로 변환하여 i값에 저장
j = list(map(int, input('end - ').split(",")))     #i에 input를 이용해 외부값을 받아 값 중간에 ,를 찍고 숫자로 변환하여 리스트로 변환하여 i값에 저장

maxx = []                                       #maxx명의 리스트 형성
for x in range(len(i)) :                        #for문을 이용해 len를 통해 i의 길이만큼 반복
    maxx.append(max([cyclelen(n) for n in range(i[x], j[x])]))  # i의 x번째 값과 j의 x번째 값만큼 반복하고 max를 이용해 사이의 사이클 길이 최대값을 계산하고 append를 이용해 maxx에 저장

print(maxx)                                     # maxx 값을 출력
print(", ".join([str(elem) for elem in maxx]))  # maxx안에 elem를 str를 통해 문자형을 변형하여 리스트에 저장하고 이를 join으로 str형으로 바꾸어 출력
                                                
#------------------------------------------------------
