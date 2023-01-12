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
def A(s1, s2):                    #def를 이용해 A명의 함수 생성
    s1 = list(s1)                 #s1를 list로 변경
    s2 = list(s2)                 #s2를 list로 변경
    if len(s1)+1 <len(s2):        #if문을 이용해 len를 통해 s1의 길이를 구하고 이 값에 1을 더한 값이 len를 이용해 구한 s2의 길이보다 크다면
        result = False            #result는 False
    elif len(s1)-1 >len(s2):      #s1의 길이에 1을 뺀 값이 s2의 길이보다 크다면
        result = False            #result는 False
    elif len(s1)+1 == len(s2):    # s1의 길이에 1을 더한 값이 s2의 길이와 같다면
        for i in range(len(s2)):  #for문을 이용해 i를 s2의 길이만큼 반복
            if not(s2[i] in s1):  #s2[i]가 s1에 없다면
                del s2[i]         #del을 이용해 s2[i] 삭제
                if s2 == s1:      #if문을 이용해 s2가 s1과 같다면
                    result = True #result는 true
                    break         #break로 탈출
                else:             #else : if 조건문의 반대/if문을 이용해 s2가 s1과 같지 않다면
                    result = False  #result는 Fasle
    elif len(s1)-1 == len(s2):    #s1길이 -1이 s2와 같다면
        idx_s1 = []               #idx_s1 명의 빈리스트 갱성
        for i in range(len(s2)):  #for문을 이용해 s2의 길이만큼 i 반복
            if not(s2[i] in s1):  #if문을 이용해 만약 s1에 s2[i]값이 없다면
                result = False    #result는 false
                break             #break로 탈출
            else:                 #if문을 이용해 만약 s1에 s2[i]값이 있다면
                idx = s1.index(s2[i]) #s2[i]가 s1의 몇번째 인덱스인지 찾고 이를 idx에 할당
                idx_s1.append(idx)    #idx_s1에 append를 통해 idx추가
        if idx_s1 == sorted(idx_s1):  #idx_s1이 만약 오름차순이먄
            result = True             #result는 true
        else:                         #오른차순이 아니라면
            result = False            #result는 false    
    elif len(s1) == len(s2):          #s1의 길이와 s2의 길이가 같다면
        cnt = 0                       #cnt 변수 생성
        for i in range(len(s2)):      #for문을 이용해 i가 s2의 길이만큼 반복된다면
            if s1[i] == s2[i]:        #만약 s[i]와 s2[i]가 같다면
                cnt +=1               #cnt에 1씩 더하여 할당
        if cnt == len(s2)-1:          #만약 cnt가 s2의 길이 -1값과 같다면 
            result = True             #result는 true
        else:                         #만약 cnt가 s2의 길이 -1값과 다르면
            result = False            #result는 False 
    return result                     #결과 반환

s1 ='cat'            #값 프린트 
s2 ='cats'
print(A(s1,s2))

#=============================================================================
#과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
#       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
#       - s1 = ‘cat’
#       - s2 =‘acts’
#       - 출력 = false

#과제 2 풀이
if __name__ == '__main__':
    s1 = list(input("s1: "))
    s2 = list(input("s2: "))
def A(s1, s2):                    #def를 이용해 A명의 함수 생성
    s1 = list(s1)                 #s1를 list로 변경
    s2 = list(s2)                 #s2를 list로 변경
    if len(s1)+1 <len(s2):        #if문을 이용해 len를 통해 s1의 길이를 구하고 이 값에 1을 더한 값이 len를 이용해 구한 s2의 길이보다 크다면
        result = False            #result는 False
    elif len(s1)-1 >len(s2):      #s1의 길이에 1을 뺀 값이 s2의 길이보다 크다면
        result = False            #result는 False
    elif len(s1)+1 == len(s2):    # s1의 길이에 1을 더한 값이 s2의 길이와 같다면
        for i in range(len(s2)):  #for문을 이용해 i를 s2의 길이만큼 반복
            if not(s2[i] in s1):  #s2[i]가 s1에 없다면
                del s2[i]         #del을 이용해 s2[i] 삭제
                if s2 == s1:      #if문을 이용해 s2가 s1과 같다면
                    result = True #result는 true
                    break         #break로 탈출
                else:             #else : if 조건문의 반대/if문을 이용해 s2가 s1과 같지 않다면
                    result = False  #result는 Fasle
    elif len(s1)-1 == len(s2):    #s1길이 -1이 s2와 같다면
        idx_s1 = []               #idx_s1 명의 빈리스트 갱성
        for i in range(len(s2)):  #for문을 이용해 s2의 길이만큼 i 반복
            if not(s2[i] in s1):  #if문을 이용해 만약 s1에 s2[i]값이 없다면
                result = False    #result는 false
                break             #break로 탈출
            else:                 #if문을 이용해 만약 s1에 s2[i]값이 있다면
                idx = s1.index(s2[i]) #s2[i]가 s1의 몇번째 인덱스인지 찾고 이를 idx에 할당
                idx_s1.append(idx)    #idx_s1에 append를 통해 idx추가
        if idx_s1 == sorted(idx_s1):  #idx_s1이 만약 오름차순이먄
            result = True             #result는 true
        else:                         #오른차순이 아니라면
            result = False            #result는 false    
    elif len(s1) == len(s2):          #s1의 길이와 s2의 길이가 같다면
        cnt = 0                       #cnt 변수 생성
        for i in range(len(s2)):      #for문을 이용해 i가 s2의 길이만큼 반복된다면
            if s1[i] == s2[i]:        #만약 s[i]와 s2[i]가 같다면
                cnt +=1               #cnt에 1씩 더하여 할당
        if cnt == len(s2)-1:          #만약 cnt가 s2의 길이 -1값과 같다면 
            result = True             #result는 true
        else:                         #만약 cnt가 s2의 길이 -1값과 다르면
            result = False            #result는 False 
    return result                     #결과 반환

print(A(s1, s2))       #프린트
#=============================================================================
