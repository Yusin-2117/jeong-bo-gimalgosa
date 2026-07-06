#제어 구조 프로그래밍

#시험 범위 외
#up & down 게임 만들기(예)
import numpy as np

np.random.seed(42)
#물론 랜덤을 사용하는 코드 연습임. 내가 걍 1트에 맞추기 위해 손본 것
#당연히 이렇게 만들면 안됨.
COM_NUM = np.random.randint(1, 50)
AT = 0

while True:
    USER_NUM = int(input("숫자를 입력하세요(1-50): "))
    AT += 1

    if USER_NUM > COM_NUM:
        print("Down ^^;")

    elif USER_NUM < COM_NUM:
        print("Up ( ﾉ ﾟｰﾟ)ﾉ")
    else:
        print(f"성공! 답은 {COM_NUM}(이)였다.")
        print(f"시도 횟수: {AT}")
        break

if AT <= 3:
    print("우수!")
elif AT <= 6:
    print("좋음!")
else:
    print("엄....www")

#함수
#1. 외장함수
#2. 내장함수
#3. 사용자정의함수

# def 함수이름(인자 X/O):
#     실행할 코드
#     return 반환값(X/O)


#예시(인자X, 반환값X)
def hello():
    print("Hello!\nwelcome to Python!")

hello()

#예시 (인자O, 반환값X)
def hello_name(name):
    print(f"Hello, {name}!\nwelcome to Python!")

hello_name("Jeon Yusin")

#예시 (인자X, 반환값O)
def hello_return():
    a = "Hello!\nwelcome to Python!"
    return a

print(hello_return())

#예시 (인자O, 반환값O)
def hello_name_return(name):
    a = f"Hello, {name}!\nwelcome to Python!"
    return a

print(hello_name_return("Jeon Yusin"))

#지역변수와 전역변수
#지역변수: 함수 내에서만 사용되는 변수
#전역변수: 함수 외부에서 사용되는 변수