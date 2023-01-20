#========================================================================
#아시다시피, 데이터는 컴퓨터에 이진수 형태로 저장됩니다. 우리가 토론할 문제는 양의 정수와 이 수의 이진 형태입니다.
#양의 정수 I가 주어지면, 당신이 할 일은 I보다 큰 수 중 가장 작은 수 J를 찾습니다. I의 이진수 형태에서의 1의 개수와 J의 이진수 형태에서의 1의 개수는 일치합니다.
#예를들어, "78"이 주어지면, 여러분은 "1001110"과 같은 이진수 형태로 쓸 수 있습니다. 이 이진수는 4개의 1을 가지고 있습니다. "1001110" 보다 크고 4개의 1을 포함하는 가장 작은 정수는 "1010011"입니다. 출력값은 "83"이 되어야 합니다.

#Input
#각 줄에 한개의 정수를 입력할 수 있습니다. (1 <= I <= 1000000)
#0이 나오면 입력을 종료합니다. 이 줄은 작업할 필요 없습니다.

#Output
#각 줄에 한개의 정수를 출력하면 됩니다.

#Sample Input
#1
#2
#3
34
#78
#0

#Sample Output
#2
#4
#5
#8
#83

#========================================================================
#과제1. 주어진 입력 수의 이진수와 동일하게 1을 가진 가장 작은 수 j와 j의 이진수 값을 출력하시오. 
#      - 조건1. j는 주어진 입력 수보단 커야한다. 
#      - input_num = 78
#      - 출력값(2진수) : 1010011
#      - 출력값(10진수) : 83

#과제 1 풀이
def is_ten_to_two(input_num):                     #def로 is_ten_to_two명의 함수 생성
    start_num = input_num                         # start_num에 input_num 저장
    two_num = ''                                  # two_num명의 빈 문자열 생성

    while start_num:                              # while문을 이용해 start_num이
        two_num += str(start_num % 2)             # two_num에 start_num 2로 나눈 나머지를 문자로 변환해 더하여 할당
        start_num = start_num // 2                # start_num에 start_num를 2로 나눈 몫을 저장
    
    return two_num[::-1]                          # two_num을 뒤집어서 return

def is_one_count(input_num):                      # def로 is_one_count명의 함수 생성 
    return is_ten_to_two(input_num).count('1')    # is_ten_to_two에 input_num 대입한 값에 count로 '1'를 세어 return

def is_the_smallest(input_num):                   #def를 이용해 is_the_smallest명의 함수 생성
    print_num = input_num                         #print_num에 input_num 저장
    for i in range(1000):                         #for문을 이용해 i를 1000번만큼 반복
        print_num += 1                            #print_num에 1씩 더하여 저장

        if is_one_count(input_num) == is_one_count(print_num): #if문을 이용해 만약 is_one_count에 input_num과 print_num를 대입한 값이 같다면,
            print(f'2진수 : {is_ten_to_two(print_num)}')        #print_num의 2진수 출력
            print(f'10진수 : {print_num}')                      #print_num 출력
            break                                              #break로 탈출

if __name__ == '__main__': 
    input_num = int(input('input = '))    # input_num에 외부값을 정수로 변환하여 저장

    if not 1 <= input_num <= 1000000:     # if문을 이용해 input_num 값이 1보다 크거나 같고 1,000,000보다 작거나 같으면
        raise Exception('잘못 입력')       # '잘못 입력' 출력

    is_the_smallest(input_num)            #is_the_smallest에 input_num 값 대입
#========================================================================
