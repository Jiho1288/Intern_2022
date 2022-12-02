"""
-----------------  Question  -----------------
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤,
문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
(예, 454 => 454, 4546793 => 454*67-9-3)
DashInsert 함수를 완성하자.

입력 - 화면에서 숫자로 된 문자열을 입력받는다. : "4546793"
출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다. : "454*67-9-3"
----------------------------------------------
"""

# 과제 1. 함수를 만들지 말고, 위 문제를 풀어보세요.
## input = "336917411"
## 출력 : 3-369-1-741-1

a = input()
len_a = len(a)

new_a = []


for i in range(len_a):

    new_a.append(a[i])


    if i==len_a-1: 
        break 
    
    else:
        if int(a[i])%2==1 and int(a[i+1])%2==1:
            new_a.append("-")
        if int(a[i])%2==0 and int(a[i+1])%2==0:
            new_a.append("*")

result = ''.join(s for s in new_a)
print(result)


#--------------------------------------------------------------------------------------------------------------


#과제 2. 함수를 만들어서 위 문제를 풀어보세요.(함수명은 "DashInsert"로 지정하세요)
## input = "13221478898889212122"
## 출력 :  1-32*21478*898*8*8921212*2

a = input()
len_a = len(a)

new_a = []


def listToString(str_list):
    result = ""
    for s in str_list:
        result += s
    return result.strip()



for i in range(len_a):

    new_a.append(a[i])


    if i==len_a-1: 
        break 
    
    else:
        if int(a[i])%2==1 and int(a[i+1])%2==1:
            new_a.append("-")
        if int(a[i])%2==0 and int(a[i+1])%2==0:
            new_a.append("*")


print (listToString(new_a))