# 점수 평균 구하기 예제
g1 = float(input("Enter your 1st game score: ")) #자료형 실수
g2 = float(input("Enter your 2nd game score: ")) 
g3 = float(input("Enter your 3rd game score: "))

avg = (g1 + g2 + g3) / 3

avg = round(avg, 2)

print(f"Your average game score is {avg}") #f-string을 이용하여 문자열 포매팅, 소수점 이하 2자리까지 반올림하여 출력



#표준 입출력 총 정리

#출력문 정리

print() #콘솔에 값을 출력하는 함수.
# 숫자, 문자열(따옴표 사용 " or '), 변수, 산술 결과(값)
# 비교연산의 값(True/False), 논리연산의 값(True/False) 출력 가능.

#python의 문자열 포매팅 사용
a = 0

#f-string 사용
print(f"123{a}456")
print("123", a, "456") #포매팅을 하지 않고 출력. 공백이 자동으로 출력

# %의 사용

# %d 사용(정수) - 10진수 정수 [말고도 %o(8진수), %x(16진수) etc.]
print("123%d456" % a)

# %i 사용(정수)
print("123%i456" % a)

# %f 사용(실수)
print("123%f456" % a)

# %s 사용(문자열)
print("123%s456" % a)

#[번외] %% 사용
# 문자열 안에서 %를 출력하고 싶을 때 사용

#[번외] 소숫점 자리수 지정
print("%.2f" % a)#소수점 이하 2자리까지 출력

#format 사용
print("123{}456".format(a))

    #사용 빈도: f-string > format > %d, %i, %f, %s

#python은 round로 반올림
#반올림은 소수점 이하 자릿수를 지정할 수 있음
print(round(3.14159, 2)) #소수점 이하 2자리까지 반올림

#올림과 내림은 math를 import 해서 사용해야 함

import math #수학 관련 함수 제공 모듈

print(math.ceil(3.2)) #올림
print(math.floor(3.2)) #내림