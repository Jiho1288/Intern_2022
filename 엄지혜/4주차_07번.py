#=============================================================================
#아래와 같은 결과를 출력하는 function을 구현하라
#bool OneEditApart(string s1, string s2)
#OneEditApart("cat", "dog") = false
#OneEditApart("cat", "cats") = true
#OneEditApart("cat", "cut") = true
#OneEditApart("cat", "cast") = true
#OneEditApart("cat", "at") = true
#OneEditApart("cat", "acts") = false
#한개의 문자를 삽입, 제거, 변환을 했을때 s1, s2가 동일한지를 판별하는 OneEditApart 함수를 작성하시오.
#=============================================================================
#과제1. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
#       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
#       - s1 = ‘cat’
#       - s2 =‘cats’
#       - 출력 = true

#과제 1 풀이
def OneEditApart(s1, s2):           # 함수 생성
    if len(s1) > len(s2):           # s1이 s2보다 길 때
        s1, s2 = s2, s1             # s1, s2를 각각 s2, s1으로 변환
    len_diff = len(s2) - len(s1)    # 두 문자의 글자 수 차이를 저장

    if len_diff > 1:                # 글자 수가 2개 이상 차이날 때
        return 'false'              # false 반환

    elif len_diff == 0:             # 문자의 길이가 같을 때 변환 가능 여부 확인
        different = 0               # 한 글자씩 비교하여 글자가 다른 경우 1씩 더할 변수
        for i in range(len(s2)):            # 한 글자씩 비교
            if s2[i] != s1[i]:              # 두 글자가 다를 때
                different += 1              # 변수에 1씩 더함
        if different <= 1:                  # 다른 글자가 1개 이하인 경우
            return 'true'                   # true 반환
        return 'false'                  # 글자가 두 개 이상 다른 경우 false 반환

    else:                           # 두 문자의 길이 차이가 1인 경우
        for j in range(len(s1)):    # 더 짧은 길이의 문자 수만큼 반복
            if s1[j] != s2[j]:      # 한 글자씩 비교했을 때 문자가 다른 경우
                s2.pop(j)           # 더 긴 문자의 해당 글자를 지운다.
                if s1 != s2:        # 그래도 두 문자가 다르다면
                    return 'false'  # false 반환
        return 'true'               # 동일한 경우 true 반환


if __name__ == '__main__':
    s1 = list(input("첫 번째 문자를 입력하세요: "))
    s2 = list(input("두 번째 문자를 입력하세요: "))
    print(OneEditApart(s1, s2))
#=============================================================================
#과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
#       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
#       - s1 = ‘cat’
#       - s2 =‘acts’
#       - 출력 = false

#과제 2 풀이
if __name__ == '__main__':
    s1 = list(input("첫 번째 문자를 입력하세요: "))
    s2 = list(input("두 번째 문자를 입력하세요: "))
    print(OneEditApart(s1, s2))
#=============================================================================
