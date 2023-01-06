"""
아래와 같은 결과를 출력하는 function을 구현하라

bool OneEditApart(string s1, string s2)

OneEditApart("cat", "dog") = false
OneEditApart("cat", "cats") = true
OneEditApart("cat", "cut") = true
OneEditApart("cat", "cast") = true
OneEditApart("cat", "at") = true
OneEditApart("cat", "acts") = false
한개의 문자를 삽입, 제거, 변환을 했을때 s1, s2가 동일한지를 판별하는 OneEditApart 함수를 작성하시오.


"""
"""
=============================================================================
과제1. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘cats’
       - 출력 = true
=============================================================================
"""

def OneEditApart(s1, s2):           
    if len(s1) > len(s2):           # s1의 길이가 s2보다 클 경우,
      for i in range(len(s1)):      # s1의 크기 만큼 for 반복문 실행
          t = s1[:i]+s1[i+1:]       # s1의 처음부터 i-1까지 s1의 i+1부터 끝까지 더한 후 t에 저장
          if s2==t: return True     # 만약 s2가 t와 같다면 oneEditApart 함수에 true 반환
      return False
    elif len(s1) < len(s2):         # s1의 길이가 s2보다 작을 경우,
      for i in range(len(s2)):      # s2 크기 만큼 for 반복문 실행
          t = s2[:i]+s2[i+1:]       # s2의 처음부터 i-1까지 s2의 i+1부터 끝까지 더한 후 t에 저장
          if s1==t: return True     # 만약 b1가 t와 같다면 true 반환
      return False
    else:                           # s1과 s2의 길이가 같을 경우,
      for i in range(len(s1)):      # s1의 길이만큼 반복
          t1 = s1[:i]+s1[i+1:]      # s1의 처음부터 i까지 s1의 i+1부터 끝까지 더한 후 t1에 저장
          t2 = s2[:i]+s2[i+1:]      # s2의 처음부터 i까지 s2의 i+1부터 끝까지 더한 후 t1에 저장
          if t1==t2: return True    # t1과 t2의 값이 같을 경우 True 반환
      return False

s1 = input('s1 = ')
s2 = input('s2 = ')
print(OneEditApart(s1, s2))         # 결과 출력


"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘acts’
       - 출력 = false
=============================================================================
"""

def OneEditApart(s1, s2):           
    if len(s1) > len(s2):           # s1의 길이가 s2보다 클 경우,
      for i in range(len(s1)):      # s1의 크기 만큼 for 반복문 실행
          t = s1[:i]+s1[i+1:]       # s1의 처음부터 i-1까지 s1의 i+1부터 끝까지 더한 후 t에 저장
          if s2==t: return True     # 만약 s2가 t와 같다면 oneEditApart 함수에 true 반환
      return False
    elif len(s1) < len(s2):         # s1의 길이가 s2보다 작을 경우,
      for i in range(len(s2)):      # s2 크기 만큼 for 반복문 실행
          t = s2[:i]+s2[i+1:]       # s2의 처음부터 i-1까지 s2의 i+1부터 끝까지 더한 후 t에 저장
          if s1==t: return True     # 만약 b1가 t와 같다면 true 반환
      return False
    else:                           # s1과 s2의 길이가 같을 경우,
      for i in range(len(s1)):      # s1의 길이만큼 반복
          t1 = s1[:i]+s1[i+1:]      # s1의 처음부터 i까지 s1의 i+1부터 끝까지 더한 후 t1에 저장
          t2 = s2[:i]+s2[i+1:]      # s2의 처음부터 i까지 s2의 i+1부터 끝까지 더한 후 t1에 저장
          if t1==t2: return True    # t1과 t2의 값이 같을 경우 True 반환
      return False

s1 = input('s1 = ')
s2 = input('s2 = ')
print(OneEditApart(s1, s2))         # 결과 출력