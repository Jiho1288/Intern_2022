#-----------------  Question  -----------------
#모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.) 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
#Example: a1b2cde3~g45hi6 → a*b*cde*~g4*hi6
#----------------------------------------------
#과제 1. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용 금지)
#       input = a1b2cde3~g45hi6
#       출력 : a*b*cde*~g4*hi6

#과제 1 풀이
origin_sentence = 'a1b2cde3~g45hi6'     #input값 origin_sentence에 저장
def digit_to_star(sentence):            # def함수를 이용해 함수 digit_to_star에 sentence 숫자가 주어진다면
    edited_sentence = ''                #edited_sentence에 문자열 생성
    for i in sentence:                  #for문을 이용하여 변수 i 반복
        if i in "1234567890":           #if문을 이용하여 문자열 내의 문자 i가 숫자라면
            if (sentence.index(i)+1) % 2 == 0:  #if문을 통해 index에 1을 더한 값이 짝수라면
                i = '*'                 #i 문자를 *로 변환
                edited_sentence += i    #edited_sentence에 i값 더하여 저장
            elif (sentence.index(i)+1) % 2 == 1: #if문을 통해 index에 1을 더한 값이 짝수라면
                edited_sentence += i    #edited_sentence에 i값 더하여 저장
        else:                           #if문을 이용하여 문자열 내의 문자 i가 숫자가 아니라면
            edited_sentence += i        #edited_sentence에 i값 더하여 저장
    return edited_sentence              #return를 이용해 edited_sentence 값 반환
print(digit_to_star(origin_sentence))   #결과값 출력
#----------------------------------------------
#과제 2. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용)
#       input = a1b2cde3~g45hi6
#       출력 : a*b*cde*~g4*hi6

#과제 2 풀이
import re                                                 #정규식 표현식 re 이용
 
def EveryOtherDigit():                                    #def를 이용해 변수 생성
    string = input("input = ")                            #string에 input을 이용하여 외부값을 받고 이룰 저장
    for i in range(len(string)):                          #for문을 이용하여 string의 길이만큼 반복
        if i % 2 == 1:                                    #if문을 사용하여 i를 2로 나눈 값이 1과 같다면
            if re.search('\d', string[i]):                #if문을 이용/re.search를 통해 일치하는 패턴 서치
                string = string.replace(string[i], '*')   #string를 string[i], '*'로 replace를 통해 바꾸어 저장

    return print(string)                                  #return를 통해 반환/string값 프린트

EveryOtherDigit()                                         # a1b2cde3~g45hi6                

#----------------------------------------------
