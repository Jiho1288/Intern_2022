#-----------------  Question  -----------------
#n개의 정수(n>0)로 이루어진 수열에 대해 서로 인접해 있는 두 수의 차가
#1에서 n-1까지의 값을 모두 가지면 그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다.
#예를 들어 다음과 같은 수열에서
#1 4 2 3
#앞 뒤에 있는 숫자 차의 절대 값이 각각 3,2,1이므로 이 수열은 유쾌한 점퍼가 된다. 어떤 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.
#Input : 각 줄 맨 앞에는 3000 이하의 정수가 있으며 그 뒤에는 수열을 나타내는 n개의 정수가 입력된다. 맨 앞 숫자가 0이면 출력하고 종료한다.
#output : 입력된 각 줄에 대해 "Jolly" 또는 "Not Jolly"를 한 줄씩 출력한다
#[Sample Input] ※ 주의: 각 줄의 맨 앞의 숫자는 수열의 갯수이다. 첫번째 입력인 4 1 4 2 3 의 맨 앞의 4는 뒤에 4개의 숫자가 온다는 것을 의미함
#4 1 4 2 3
#5 1 4 2 -1 6
#[Sample Output]
#Jolly
#Not jolly
#----------------------------------------------
#과제 1. 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.
#       input = ["4 1 4 2 3", "5 1 3 2 -1 6"]
#       출력 : Jolly
#             Not Jolly

#과제 1 풀이
def sub(a, b):              #def 함수를 이용해 함수 add에 입력값으로 a, b를 받음
    return abs((b - a))     #return을 이용해 b에 a를 뺀 값임

value = list(map(int, input("입력시킬 개수와 수열을 입력하세요 : ").split()))  # input을 통해 외부값을 입력받고 이를 숫자로 변환하여 리스트에 저장하여 value에 할당

n = value[0]                #value[0]을 n에 저장 
sequence = value[1:]        #seqence에  value[1:] 저장

if n == 0:                  #if문을 이용하여 n이 0이라면
    print("0")              #"0" 출력

elif n != len(sequence):    # n이 sequence의 길이 값과 같지 않다면 
    print("입력시킬 개수와 수열의 개수가 맞지 않습니다.") #"입력시킬 개수와 수열의 개수가 맞지 않습니다." 출력

else:                       #if문을 이용하여 n이 0이 아니라면
    requirement = list(range(sequence[0],sequence[1])) #sequence의 0을 대입한 값부터 1을 대입한 값 -1 까지의 범위를 리스트로 requirement에 저장
    sublist = []            #sublist 명의 리스트 생성

    for i in range(len(sequence)):  #for 문을 통해 len를 이용하여 sequence 길이 만큼 반복
        subvalue = sub(sequence[i],sequence[i+1])  # subvalue에 sequence에 i를 대입한 값, sequence에 i+1를 대입한 값을 저장
        sublist.append(subvalue)    #subvalue값을 sublist를 추가하여 저장
        if i == len(sequence) - 2:  #if문을 이용해 squence 길이에 -2를 한 값이 i 값과 같다면
            break                   #정지

    if list(set(sublist)) == requirement: #if문을 이용해 requirement값이 list(set(sublist))와 같다면
        print("Jolly")                    #Jolly 출력
    else:                                 #if문을 이용해 requirement값이 list(set(sublist))와 같지 않다면
        print("Not Jolly")                #Not Jolly 출력

#----------------------------------------------
#과제 2. 수열이 jolly jumper인지 판단할 수 있는 프로그램을 작성하시오.
#       input = ["4 1 4 2 3", "5 1 3 2 -1 6", "0"]
#       출력 : Jolly
#             Not Jolly
#             0

#과제 2 풀이
def sub(a, b):              #def 함수를 이용해 함수 add에 입력값으로 a, b를 받음
    return abs((b - a))     #return을 이용해 b에 a를 뺀 값임

value = list(map(int, input("입력시킬 개수와 수열을 입력하세요 : ").split()))  # input을 통해 외부값을 입력받고 이를 숫자로 변환하여 리스트에 저장하여 value에 할당

n = value[0]                #value[0]을 n에 저장 
sequence = value[1:]        #seqence에  value[1:] 저장

if n == 0:                  #if문을 이용하여 n이 0이라면
    print("0")              #"0" 출력

elif n != len(sequence):    # n이 sequence의 길이 값과 같지 않다면 
    print("입력시킬 개수와 수열의 개수가 맞지 않습니다.") #"입력시킬 개수와 수열의 개수가 맞지 않습니다." 출력

else:                       #if문을 이용하여 n이 0이 아니라면
    requirement = list(range(sequence[0],sequence[1])) #sequence의 0을 대입한 값부터 1을 대입한 값 -1 까지의 범위를 리스트로 requirement에 저장
    sublist = []            #sublist 명의 리스트 생성

    for i in range(len(sequence)):  #for 문을 통해 len를 이용하여 sequence 길이 만큼 반복
        subvalue = sub(sequence[i],sequence[i+1])  # subvalue에 sequence에 i를 대입한 값, sequence에 i+1를 대입한 값을 저장
        sublist.append(subvalue)    #subvalue값을 sublist를 추가하여 저장
        if i == len(sequence) - 2:  #if문을 이용해 squence 길이에 -2를 한 값이 i 값과 같다면
            break                   #정지

    if list(set(sublist)) == requirement: #if문을 이용해 requirement값이 list(set(sublist))와 같다면
        print("Jolly")                    #Jolly 출력
    else:                                 #if문을 이용해 requirement값이 list(set(sublist))와 같지 않다면
        print("Not Jolly")                #Not Jolly 출력

#----------------------------------------------
