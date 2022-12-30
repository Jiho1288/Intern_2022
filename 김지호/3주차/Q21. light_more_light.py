n = input('n번째 전구 숫자:')  #먼저 n이라는 변수에 전구 숫자를 입력 받고

n_list = n.split(' ')

for j in range(len(n_list)):
    int_n = int(n_list[j])
    switch = "no"                      #switch의 초기상태를 no 즉 꺼진 상태로 초기화

    for i in range(1,int_n+1):              #1부터 n까지 for문을 사용하여 반복
        if int_n%i==0:                      #i가 n에 나눠떨어진다면
            if switch == "no":         #다중조건문을 사용하여 기존의 스위치가 no면 yes로 바꾸고
                switch = "yes"            
            else:                       #기존의 스위치가 yes면 no로 바꿔서 결과를 출력
                switch = "no"

    print(switch)
