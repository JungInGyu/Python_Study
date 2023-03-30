# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
# num = 100
num = 100
num = str(num)
print(num,type(num))
# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
st_fl = "15.79"
st_fl = float(st_fl)
print(st_fl,type(st_fl))
# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
# year = "2020"
year = "2020"
year = int(year)
for i in range(0,3):
    year+=1
print(year,type(year))