## 산술연산자
# + - * /
# //(몫) %(나머지) **(거듭제곱)

print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)

print(11 // 3)  # 3
print(11 % 3)  # 2

# 5는 홀수 -> 2로 나눴을 때 나머지가 1이면 홀수

print(10**5)

#### 연산자 우선순위
# **, * / // %, + -
print(2 + 5 * 3)  # 17
print((2 + 5) * 3)  # 21

### 문자열 연산
print("*" * 20)
print("안녕" + "하세요" + "!!!")

### 복합 할당 연산자
score = 70
score = score + 30  # = score += 30 -> 100
score += 30  # 130
print("score", score)

score = 70
score = score - 30  # 40
score -= 30  # 10
print("score", score)

# 실습5
x = 10
print(x)  # 10
x = x + 5
print(x)
x = x * 2
print(x)

# 실습6
a = 100
b = a
a = 999
print(a)
print(b)

# 실습7
temp = 25
print(temp)
score = 90
print(score)

# 실습8
temp = 25  # 온도(섭씨)
# count = 3 # 센서 계수
print(temp)

# 실습9
x = 5
x = 10
x = x + 1
print(x)  # 11

# 실습10
name = "센서A"  # 글자
temp = 25  # 숫자
print("설비")
print(name)
print(temp)

# 실습11
a = 25
b = 3
device_temp = a
sensor_count = b
print(device_temp)

# 실습12
x, y, z = 1, 2, 3
width, height = 4, 3
print(width)
print(height)
print("삼각형 넓이:", width * height / 2)  # 6.0

# 실습 1
count = 3  # int
print(count)
temp = 25.5  # float
print(temp)
name = "센서a"  # str
print(name)
is_ok = True  # bool
print(count < temp)

# 실습2

print(type(count))  # <class 'int'>
print(type(temp))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_ok))  # <class 'bool'>

# 실습3
print(type(100))  # <class 'int'>
print(type(100.0))  # <class 'float'>
print(type("100"))  # <class 'str'>

# 실습4
print(80 + 90)  # 170
print("80" + "90")  # 8090
print(type(80 + 90))  # <class 'int'>
print(type("80" + "90"))  # <class 'str'>

# 실습5
# 3>2 = True
ok = True  # bool
no = False  # bool
print(3 > 2)
print(5 == 5)
print(type(3 > 2))  # <class 'bool'>

# 실습6
count = 8
print(type(count))  # <class 'int'>
count = 8.0
print(type(count))  # <class 'float'>
count = "문자"
print(type(count))  # <class 'str'>

# 실습7
device_temp = 8.0  # 실수
check_count = 8  # 정수
device_name = "팔"  # 문자열
is_normal = True  # 논리합

# 11-18
# ======== 비교, 논리 연산자 ========
# ==(같다) !=(다르다), >= <= > <
# and or not
number1 = 3
number2 = 5

print(number1 <= number2)  # True
print(number1 >= number2)  # False
print(number1 == number2)  # False
print(number1 != number2)  # True

print("=======")
print(True and True and True and False)  # False
print(True or True or True or False)  # True
print(not (True or True or True or False))  # False
print((True and True) and (True or False))  # True

temp = 80
print(temp > 80 and temp < 100)  # False
print(not (temp > 90))  # True
