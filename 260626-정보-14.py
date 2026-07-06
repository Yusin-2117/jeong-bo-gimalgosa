#Global

count = 0 
def add(a, b):
    global count #지역변수를 전역변수로
    c = a + b
    print(f"{a}+{b}={c}")
    count += 1

add(3,5)
add(10,14)
print(f"덧셈 횟수: {count}")

#모듈&라이브러리

import math #수학관련 기능 제공
print(math.gcd(15, 18))#최대공약수

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #as로 별칭을 지정하여 사용 가능


#146page

import matplotlib.pyplot as plt

item = ['mobile', 'delivery', 'trip', 'shopping']
cost = [75000, 138450, 94800, 100500]

#원그래프
#plt.pie(cost, labels=item, autopct='%.2f%%') #autopct는 백분율 표시, %.2f는 소수점 두 자리까지 표시
#막대그래프
#plt.bar(item, cost)
#막대그래프(가로)
#plt.barh(item, cost)
#선그래프
#plt.plot(item, cost)
#산점도
#plt.scatter(item, cost)
#히스토그램
plt.hist(cost, bins=4)#bins는 막대의 개수
#박스플롯
#plt.boxplot(cost)
#채우기 그래프
plt.fill_between(item, cost)
#채우기 그래프 x
plt.fill_betweenx(item, cost)
#바이오린플롯
#plt.violinplot(cost)
plt.show()