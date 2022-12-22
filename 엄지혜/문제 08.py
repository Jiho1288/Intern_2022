#--------------------------------------------------------------------------------------------------------------
# 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호이다.
# 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
# 예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
# 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라
#--------------------------------------------------------------------------------------------------------------

# 과제 1. 대문자로 구성된 단어 1개를 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "ICL"
## n = 3
## 출력 : LFO

#과제 1 풀이 
def enig(inp, n) :                                                        # def()함수로 enig 함수 생성
    s, res = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ', ''   # s에 알파벳 대문자 소문자 저장, res에 ''저장
    for M in inp :                                      # for문으로 inp문 반복
        if M in s : res += s[(s.index(M)+2*n)%52]       # if문으로 M이 s에 있다면, res에 s[(25+2*n)%52] 값 더하기
        else : res += M                                 # else 문으로 res에 M을 더함
    return res                                          # res 값 반환
INP = str(input("INPUT = "))                            # input로 외부값을 받고 이를 문자로 변환하여 INP에 저장
N = int(input("N = "))                                  # input로 외부값을 받고 이를 숫자로 변환하여 N에 저장
print(enig(INP, N))                                     # enig 함수를 실행 후 출력

#--------------------------------------------------------------------------------------------------------------
# 과제 2. 대문자와 소문자로 구성된 단어 1개를 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "Library"
## n = 5
## 출력 : Qngwfd

#과제 2 풀이
def enig(inp, n) :                                                        # def()함수로 enig 함수 생성
    s, res = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ', ''   # s에 알파벳 대문자 소문자 저장, res에 ''저장
    for M in inp :                                      # for문으로 inp문 반복
        if M in s : res += s[(s.index(M)+2*n)%52]       # if문으로 M이 s에 있다면, res에 s[(25+2*n)%52] 값 더하기
        else : res += M                                 # else 문으로 res에 M을 더함
    return res                                          # res 값 반환
INP = str(input("INPUT = "))                            # input로 외부값을 받고 이를 문자로 변환하여 INP에 저장
N = int(input("N = "))                                  # input로 외부값을 받고 이를 숫자로 변환하여 N에 저장
print(enig(INP, N))                                     # enig 함수를 실행 후 출력

#--------------------------------------------------------------------------------------------------------------
# 과제 3. 대문자와 소문자를 포함하는 문장을 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "MMy subject is Library & Information Science."
## n = 2
## 출력 : Oa uwdlgev ku Nkdtcta & Kphqtocvkqp Uekgpeg.

#과제 3 풀이
def enig(inp, n) :                                                        # def()함수로 enig 함수 생성
    s, res = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ', ''   # s에 알파벳 대문자 소문자 저장, res에 ''저장
    for M in inp :                                      # for문으로 inp문 반복
        if M in s : res += s[(s.index(M)+2*n)%52]       # if문으로 M이 s에 있다면, res에 s[(25+2*n)%52] 값 더하기
        else : res += M                                 # else 문으로 res에 M을 더함
    return res                                          # res 값 반환
INP = str(input("INPUT = "))                            # input로 외부값을 받고 이를 문자로 변환하여 INP에 저장
N = int(input("N = "))                                  # input로 외부값을 받고 이를 숫자로 변환하여 N에 저장
print(enig(INP, N))                                     # enig 함수를 실행 후 출력

#--------------------------------------------------------------------------------------------------------------
