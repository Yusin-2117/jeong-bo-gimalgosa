#python 표준 입출력

#출력
print()
#입력 
input() #기본적으로 str로 입력받음 -> 자료형 변환 필요

#예제1 - 교육과정 외 개념 포함(5/26기준)

name = input("Pls enter your name: ") #이름을 입력 받아 name에 저장(입력)

while True:
    By = int(input("Pls enter your birth year: ")) #자료형을 int로 By에 저장(입력) By: birth year

    if By > 2026 or By < 1900: #잘못된 입력 처리
        print("잘못된 입력")
        continue #계속 반복
    
    break #반복 종료

age = 2026 - By + 1 #korean age(만 나이)를 계산

print(f"Hello {name}, you are {age} years old")#출력, format을 사용하여 문자열에 삽입



weight = float(input("Pls enter your weight: ")) #몸무게를 입력 받아 weight에 저장(입력)
height = float(input("Pls enter your height: ")) #키를 입력 받아 height에 저장(입력)

bmi = weight / (height / 100) ** 2
info = ""

if bmi < 18.5:
    info = "Underweight"
elif bmi < 23:
    info = "Normal"
elif bmi < 25:
    info = "Overweight"
else:
    info = "Obesity"

print(f"Your BMI is {bmi}, and your status is {info}")
