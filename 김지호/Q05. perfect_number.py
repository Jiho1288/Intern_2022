"""
-----------------  Question  -----------------
자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
예를 들면, 6과 28은 완전수이다.
6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수
입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.
----------------------------------------------
"""
# 과제 1
## input = "10000"
## 출력: 6, 28, 496, 8128

max_num = int(input("input: "))


for i in range(max_num):
    test_num = i+1


    divisor_list = []     

    for j in range(1,test_num):
   
        if test_num%j == 0:
            divisor_list.append(j)

    if sum(divisor_list)==test_num:
        print(test_num, end=", ")

