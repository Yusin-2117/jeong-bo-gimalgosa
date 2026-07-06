#프로그래밍수행2420전유신.ipynb

#코랩에서 파일 불러오기:
#from google.colab import files
#files.upload()

#비식별화: .replace()말고 -> 슬라이싱

#while True
'''a = 1
while True: #while 1도 무한 반복 사용 가능
    print(a)
    a += 1
'''

#break
while True:
    n = input("프로그램을 종료하려면 'Q'를 누르시오")
    if n == 'Q':
        break

#contiune
total = 0
for i in range(1, 101):
    if i % 5 != 0:
        continue
    total += i
print(total)

sum = 0
for i in range(5, 101, 5):
    sum += i 

print(sum)