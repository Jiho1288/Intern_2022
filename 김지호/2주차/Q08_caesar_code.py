"""
시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호이다.
예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라.
"""


"""
==========================================================================
# 과제 1. 대문자로 구성된 단어 1개를 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "ICL"
## n = 3
## 출력 : LFO
==========================================================================
"""

print("***과제1***")

word = input("input=")      # 입력받은 대문자 단어 word 변수에 저장

n = input("n=")             # 입력받은 n값 n 변수에 저장

word_list = list(word)      # string으로 구성된 word를 list로 word_list 변수에 저장

result = ""                 # 결과 값에 대한 변수 설정

for i in range(len(word_list)):                     # 반복문을 통해 word_list에 저장된 각각의 element에 접근

    upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  # 대문자 순서 정보에 대한 list를 upper_case 변수에 저장

    word_index = upper_case.index(word_list[i])     # word_list의 element가 몇번째 알파벳인지 upper_case.idex를 통해 확인

    upper_case = upper_case + upper_case            # 알파벳 순서에 n을 더했을때 "Z"를 넘어가는 경우를 대비해 upper_case lis를 연속해서 두번 나열

    changed_word = upper_case[word_index + int(n)]  # 알파벳 순서에 n을 더했을때의 변경된 알파벳 값을 changer_word 변수에 대입

    result += changed_word                          # 결과값 차례대로 result 변수에 저장

print(result)


"""
==========================================================================
# 과제 2. 대문자와 소문자로 구성된 단어 1개를 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "Library"
## n = 5
## 출력 : Qngwfwd
==========================================================================
"""

print("\n***과제2***")

word = input("input=")

n = input("n=")

word_list = list(word)

result = ""

for i in range(len(word_list)):

    upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  # 대문자 순서 정보에 대한 list를 upper_case 변수에 저장

    lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  # 소문자 순서 정보에 대한 list를 lower_case 변수에 저장

    if word_list[i].isupper():                      # 확인할 문자가 대문자일 경우

        word_index = upper_case.index(word_list[i])

        upper_case = upper_case + upper_case

        changed_word = upper_case[word_index + int(n)]

        result += changed_word
    
    elif word_list[i].islower():                    # 확인할 문자가 소문자일 경우

        word_index = lower_case.index(word_list[i])

        lower_case = lower_case + lower_case

        changed_word = lower_case[word_index + int(n)]

        result += changed_word

print(result)


"""
==========================================================================
# 과제 3. 대문자와 소문자를 포함하는 문장을 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "My subject is Library & Information Science."
## n = 2
## 출력 : Oa uwdlgev ku Nkdtcta & Kphqtocvkqp Uekgpeg.
==========================================================================
"""

print("\n ***과제3***")

word = input("input=")

n = input("n=")

word_list = list(word)

result = ""

for i in range(len(word_list)):

    upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  # 대문자 순서 정보에 대한 list를 upper_case 변수에 저장

    lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  # 소문자 순서 정보에 대한 list를 lower_case 변수에 저장

    if word_list[i].isupper():                      # 확인할 문자가 대문자일 경우

        word_index = upper_case.index(word_list[i])

        upper_case = upper_case + upper_case

        changed_word = upper_case[word_index + int(n)]

        result += changed_word
    
    elif word_list[i].islower():                    # 확인할 문자가 소문자일 경우

        word_index = lower_case.index(word_list[i])

        lower_case = lower_case + lower_case

        changed_word = lower_case[word_index + int(n)]

        result += changed_word

    else:                                           # 확인할 문자가 그 외 일 경우 (공백 또는 기타 부호 등) 그대로 출력
        result += word_list[i]

print(result)

# reference1: https://coincidence24.tistory.com/18
# index 확인 함수

# reference2 : https://codechacha.com/ko/python-lower-upper/ 
# isupper 함수
