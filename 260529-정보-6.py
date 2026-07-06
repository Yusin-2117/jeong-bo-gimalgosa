#이스케이프 문자(\n, \t, \\, \' etc)
print("Hello\nWorld") 

    #따옴표 출력
print("Hello\"World\"") #컴퓨터는 \'를 '로 인식
print('Hello\'World\'')
print("Hello'World'") #따옴표를 출력하려면 다른 종류의 따옴표로 감싸거나 \를 이용하여 이스케이프 문자로 사용해야 함
print('Hello"World"')

#sep → 출력값 사이에 들어가는 문자열(기본값은 공백)
#end → 출력이 끝난 뒤 붙는 문자열 (기본값은 줄바꿈 \n)

#sep(구분)
print("Hello", "World", sep="-") #-로 대체

#end(끝)
print("Hello", end = " ") #공백으로 대체
print("World")

f = open(r"C:\Users\yn17j\OneDrive\바탕 화면\VS\정보\버킷리스트.csv", "r", encoding="utf-8") # r: 읽기, encoding: 인코딩 방식 utf-8 -> 한글
# raw string: 문자열 앞에 r을 붙이면 이스케이프 문자를 무시하고 그대로 출력
data = f.read() #read(): 파일 전체를 읽어서 문자열로 반환
print(data)
f.close()

#추가하기(append)

data = input("추가할 내용: ")
f = open(r"C:\Users\yn17j\OneDrive\바탕 화면\VS\정보\버킷리스트.csv", "a", encoding="utf-8") # a: 추가, encoding: 인코딩 방식 utf-8 -> 한글
f.write("\n" + data)
f.close()

# 읽기(r)
# 추가하기(a)
# 덮어쓰기(w)