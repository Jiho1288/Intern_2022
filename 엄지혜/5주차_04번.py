#========================================================================
#4개의 직사각형이 평면에 있는데 밑변이 모두 가로축에 평행하다. 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고 겹쳐 있을 수도 있다.
#또한 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭지점이 겹쳐질 수도 있다.

#입력형식
#하나의 직사각형은 왼쪽 아래의 꼭지점과 오른쪽 위의 꼭지점의 좌표로 주어진다. 입력은 네 줄이며, 각 줄은 네 개의 정수로 하나의 직사각형을 나타낸다.
#첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭지점의 x좌표, y좌표이다.
#단, x좌표와 y좌표는 1 이상이고 1000 이하인 정수이다.

#출력형식
#화면에 4개의 직사각형이 차지하는 면적을 출력한다.

#입력예제
#1 2 4 4
#2 3 5 7
#3 1 6 5
#7 3 8 6

#출력예제
#26
#========================================================================
#과제1. input1과 input2로 구성되는 두 직사각형이 차지하는 넓이를 구하시오.
#      - 조건 1 : 첫 번째와 두 번째 정수는 사각형 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 오른쪽 위 꼭지점의 x좌표, y좌표이다.
#      - 조건 2 : 직사각형의 면적이 겹칠 경우, 중복하여 계산하지 않는다.
#      - rectangle1 = '1 2 4 4'
#      - rectangle2 = '2 3 5 7'
#      - 출력값 : 16

#과제 1 풀이
def fill_plane(plane, coordinate):                      #def를 통해 plane과 coordinate값을 받은 fill_plane명 함수 생성
    for x in range(coordinate[0],coordinate[2]):        #for문으로 x을 coordinate의 0번째 수부터 coordinate 2번째 수까지 반복
        for y in range(coordinate[1],coordinate[3]):    #for문으로 y을 coordinate의 1번째 수부터 coordinate의 3번째 수까지 반복
            plane[y][x] = 1                             #plane[y][x]는 1 

Plane = [[0]*1000 for x in range(1000)]                 #plane에 [0]*1000/for문을 이용해 x를 1000만큼 반복

rectangle1 = input('rectangle1 = ')                     #rectangle1에 rectangle1 값을 받아 저장/2와 차이점
rectangle2 = input('rectangle2 = ')                     #rectangle2에 rectangle2 값을 받아 저장/2와 차이점

rectangle_list = []                                     #rectangle_list명의 빈리스트 생성

rectangle_list.append(rectangle1)                       #rectangle_list에 rectangle1 값을 추가/2와 차이점
rectangle_list.append(rectangle2)                       #rectangle_list에 rectangle2 값을 추가/2와 차이점
print(rectangle_list)                                   #rectangle_list 프린트/2와 차이점

for x in rectangle_list:                                #for문으로 x를 rectangle_list만큼 반복
    coordinate = [int(c) for c in x.split()]            #coordinate에 c를 int로 정수로 변환/for문을 이용하여 c를 x만큼 반복/' '로 구분하여 저장
    fill_plane(Plane,coordinate)                        #fill_plane(Plane,coordinate)

Area = sum([sum(x) for x in Plane])                     #Area에 for문을 이용하여 x를 Plane만큼 반복할 때, x의 합의 합

#========================================================================
#과제2. 아래의 입력인 4개의 직사각형이 차지하는 넓이를 구하시오.(직사각형이 겹치거나 또 다른 하나가 다른 하나를 포함할 수 있음)
#      - 조건 1 : 첫 번째와 두 번째 정수는 사각형 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 오른쪽 위 꼭지점의 x좌표, y좌표이다.
#      - 조건 2 : 직사각형의 면적이 겹칠 경우, 중복하여 계산하지 않는다.      
#      - rectangle_list = ['1 2 4 4','2 3 5 7','3 1 6 5','7 3 8 6']
#      - 출력값 : 26

#과제 2 풀이
def fill_plane(plane, coordinate):                      #def를 통해 plane과 coordinate값을 받은 fill_plane명 함수 생성
    for x in range(coordinate[0],coordinate[2]):        #for문으로 x을 coordinate의 0번째 수부터 coordinate 2번째 수까지 반복
        for y in range(coordinate[1],coordinate[3]):    #for문으로 y을 coordinate의 1번째 수부터 coordinate의 3번째 수까지 반복
            plane[y][x] = 1                             #plane[y][x]는 1 

Plane = [[0]*1000 for x in range(1000)]                 #plane에 [0]*1000/for문을 이용해 x를 1000만큼 반복

a,b,c,d = input('rectangle_list = ').split(',')        #a, b, c, d에 rectangle_list을 받고 ','를 기준을 구분하여 할당/1과 차이점 

rectangle_list = []                                     #rectangle_list명의 빈리스트 생성

rectangle_list.append(a)                                #rectangle_list에 a 추가/1과 차이점
rectangle_list.append(b)                                #rectangle_list에 b 추가/1과 차이점
rectangle_list.append(c)                                #rectangle_list에 c 추가/1과 차이점
rectangle_list.append(d)                                #rectangle_list에 d 추가/1과 차이점

for x in rectangle_list:                                #for문으로 x를 rectangle_list만큼 반복
    coordinate = [int(c) for c in x.split()]            #coordinate에 c를 int로 정수로 변환/for문을 이용하여 c를 x만큼 반복/' '로 구분하여 저장
    fill_plane(Plane,coordinate)                        #fill_plane(Plane,coordinate)

Area = sum([sum(x) for x in Plane])                     #Area에 for문을 이용하여 x를 Plane만큼 반복할 때, x의 합의 합

#========================================================================
#과제 1 출력
print('출력값 : ', Area) 
#과제 2 출력
print('출력값 : ', Area) 
#========================================================================
