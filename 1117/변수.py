# 변수 선언
# 변수_이름 - 할당할값
# = (등호 표시) : 같다는 의미가 아닌 대입을 의미
temp = 25
name = "센서A"
print(temp)
print(name)

x = 10
print("처음 할당된후의 x:", x)
x = 15
print("재할당된 후의 x:", x)

x = x + 5  # 직전의 x(15)를 연산하여 다시 x에 대입
print("연산후의 x:", x)

## 변수이름 규칙
# 숫자로 시작되면 안됨, 특수문자는 언더바(_)만 허용이 됨
# 파이썬에서는 변수명 규칙을 snake_case 를 사용하도록 권장됨
# 변수명엔 공백 있을 수 없음
# 2sensor=10 -> 숫자부터 시작되면 안됨
sensor_count = 3  # snake_case, python 변수명 짓기 규칙
sensorCount = 3  # camelCase, 에러는 아니지만 권장되진 않습니다.
print(sensor_count, sensorCount)

temp2 = 25
print(temp2)

# if = 15 # if, for, False 같은 예약어는 변수 이름으로 사용할 수 없음

## 대소문자도 변수명에서 구분된다.
temp = 10
Temp = 100
print("temp, Temp", temp, Temp)

score = 50
score = 70
score = 90
print("score:", score)

## 다른 변수의 값 담기
# alt shift 방향키(위/아래) -> 줄 복사
a = 10
b = a
a = 11
print("a:", a)
print("b:", b)

## 변수 선언 할줄에 여러개 하자
width, height = 4, 3
print("가로: ", width)
print("세로: ", height)
print("직사각형의 넓이: ", width * height)

# x, y = 1, 2, 3 #ValueError: too many values to unpack

# NameError
value = 15  # 먼저 정의가 되어있어야
print(value)  # 사용할 수 있음

# 실습 11-17

# 실습1
temp = 25
print(temp)
name = "센서A"
print(name)

# 실습2
temperature = 30
print(temperature)

# 실습3
my_number = 8
print(my_number)
mood = "행복"
print(mood)

# 실습4
age = 27
label = "나이"
print(label)
print(age)
