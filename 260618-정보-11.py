#조건문 if, elif, else

print("과속 단속구역 통과 중")
speed = int(input("현재 속도: "))

if speed > 60:
    O_speed = speed - 60
    print(f"과속입니다. 속도를 {O_speed}km/h 줄이시오")

else:
    print("정상 속도에 준수합니다.")

# 중첩 조건문

#if 조건A:
#    if 조건 B:
#        실행문
#    else:
#        실행문

print("주행중인 도로를 입력하시오")
road = int(input("도로(일반도로, 1 / 고속도로, 2): "))

if road == 2:
    lim = 100

else:
    protection = int(input("안전운전 단속 구역 여부 (단속구역, 1 / 일반구역, 2): "))
    if protection == 1:
        lim = 30
    else:
        lim = 50

print(f"제한 속도는 {lim}km/h입니다.")

#다중 조건문

#if 조건A:
#    실행문
#elif 조건B:
#    실행문
#else:
#    실행문

score = int(input("수학과목 모의고사 점수를 입력: "))

#Q. 잘못된 예
if score >= 40:
    print(" 1등급")
if score >= 35:
    print(" 2등급")
if score >= 30:
    print(" 3등급")
else:
    print("상종 안함")

# A. 이 코드는 잘못된 코드이다. if문이 독립적으로 작동하기 때문에 30점 이상이면 1등급과 3등급이 모두 출력된다.

#Q. 올바른 예
if score >= 40:
    print("1등급")
elif score >= 35:
    print("2등급")
elif score >= 30:
    print("3등급")
else:
    print("상종 안함")

# A. 이 코드는 올바른 코드이다.
# Q. 문제는 50보다 큰 수를 넣어도 1등급이 출력된다.
if 0 <= score <= 50:
    if score >= 40:
        print(" 1등급")
    elif score >= 35:
        print(" 2등급")
    elif score >= 30:
        print(" 3등급")
    else:
        print("상종 안함")

else:
    print("잘못된 입력입니다.")
# A. 중첩 반복문을 사용하여 문제를 해결할 수 있다.

#반복문 for, while

#for문
for i in [1,2,3]:
    print(i) # i는 변수이므로 다른 문자로 대체 가능 

exam_sub = ['국어', '영어', '수학', '사회', '과학'] #리스트가 들어갈 수 있음

for i in exam_sub:
    print(i+"영역")

for i in 'soccer':
    print(i, 'team KOR')

# range()함수

for i in range(10):
    print(i)
# 반복되어 1부터 9까지 출력
 
# range(시작, 끝값+1, 증감값)
# for i in range()의 경우, print문 사용 시 i와 관련된 연산만 작용하고 나머지는 문자 취급

d = int(input("구구단 단수를 입력: "))

for i in range(1,10):
    a = d * i
    print(d, "X", i, "=", a)

#==========================
# 132p 중첩 for문 : 기말 고사
#==========================

for i in range(1,4):
    for j in range(5,8):
        print(i,j)
# 실행값: 1 5, 1 6, 1 7, 2 5, 2 6, 2 7, 3 5, 3 6, 3 7
# i = 1, 2, 3
# j = 5, 6, 7
# i는 1일 때 j는 5,6,7까지 출력
# i는 2일 때 j는 5,6,7까지 출력
# i는 3일 때 j는 5,6,7까지 출력

for i in range(2, 10):
    print("")
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")
        #"%d * %d = %d" % (i, j, i*j)

#while문
a = 1

while a <= 5:
    print(a)
    a+=1

# 다음 시간 무한 반복