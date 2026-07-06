#다차원 데이터 구조

# list(리스트): 여러가지 데이터를 하나의 변수에 저장할 수 있음.

# 1차원 리스트

# 기존 변수의 문제점
# 1. 변수가 너무 많아짐
# 2. 관리가 어려움
# 3. 반복 작업의 어려움

# 리스트 명 = [값1- 인덱스 0번, 값2, 값3, ...]
score = [85, 70, 95, 88, 81]
print(f'list_score = {score}') #전체 출력
print(f'list_score[0] = {score[0]}') #인덱스로 특정 위치의 데이터 접근 가능

score_1 = 100
score_2 = [100, 98, 86]
score = [85, 70, '구십 오', 88, score_1, score_2]
print(f'list_score = {score}') #리스트 내부의 데이터도 다른 데이터 type을 가질 수 있음

#슬라이싱
fruits = ['apple', 'banana', 'orange', 'melon']
print(fruits[0]) #apple
print(fruits[0:2]) #apple & banana
print(fruits[1:]) #banana & orange & melon
# :를 이용하여 범위 지정 가능(시작:끝(미포함), 시작:, :끝)
# 두 개 이상이나 영역으로 출력 시 []/""/,도 함께 출력됨
