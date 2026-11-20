######## [1] 문자열 종합 실습 #########
"""
1. WARNING이 몇 번 나타나는지 출력
2. NORMAL이 몇 번 나타나는지 출력
3. ERROR가 몇 번 나타나는지 출력
4. 첫 번째 WARNING의 시작 위치를 구하기
5. 두 번째 WARNING의 시작 위치를 구하기
6. 첫 번째 WARNING의 끝 위치와 두 번째 WARNING의 시작 위치 사이에 몇 글자가 있는지 구하기
7. 두 WARNING 사이에 들어 있는 문자열만 추출하세요.
8. 7번에서 추출한 문자열에 ERROR가 포함되어 있는지 확인하세요.
"""

prac1 = "NORMAL-WARNING-NORMAL-ERROR-WARNING"

# 1~3
count_warning = prac1.count("WARNING")
count_normal = prac1.count("NORMAL")
count_error = prac1.count("ERROR")
print(count_warning, count_normal, count_error)

# 4~5
first_idx = prac1.find("WARNING")
second_idx = prac1.rfind("WARNING")
second_idx_2 = prac1.find("WARNING", first_idx + 1)
print(first_idx)
print(second_idx, second_idx_2)

# 6. 첫 번째 WARNING의 끝 위치와 두 번째 WARNING의 시작 위치 사이에 몇 글자가 있는지 구하기
first_end = first_idx + len("WARNING")
distance = second_idx - first_end
print("warning 사이의 문자 수", distance)

# 7. 두 WARNING 사이에 들어 있는 문자열만 추출하세요.
between_warning = prac1[first_end:second_idx]
print("warning 사이의 문자열", between_warning)

# 8. 7번에서 추출한 문자열에 ERROR가 포함되어 있는지 확인하세요.
has_error = "ERROR" in between_warning
print("ERROR 포함 여부:", has_error)

######## [1] 연산자 실습 #########
# 실습 1
a = 17
b = 5
print("덧셈", a + b)
print("뺄셈", a - b)
print("곱셈", a * b)
print("나눗셈", a / b)
print("몫 구하기", a // b)
print("나머지 구하기", a % b)
print("거듭제곱", a**b)

### 실습2
# a = int(input("자연수를 입력해주세요."))
# b = int(input("자연수를 입력해주세요."))
# c = int(input("자연수를 입력해주세요."))
a, b, c = 3, 3, 3
# 평균 구하기
print("평균:", (a + b + c) / 3)
# 직육면체 부피 구하기
print("직육면체 부피:", a * b * c)

### 실습5
total = 500  # 전체 생산량
defect = 23  # 불량품 수

running_time = 21  # 가동 시간
entire_time = 24  # 전체 시간

# 불량률
defect_rate = defect / total * 100
# 가동률
running_rate = running_time / entire_time * 100
print("불량률:", defect_rate, "가동률:", running_rate)

### 실습 6
minutes = 500
hours = minutes // 60
min = minutes % 60
print(hours, "시간", min, "분")

### 실습 8
temp = 85
pressure = 5

# 60이상 90이하일 때 온도 정상
temp_ok = temp >= 60 and temp <= 90

# 3이상 7이하일 때 압력 정상
pressure_ok = pressure >= 3 and pressure <= 7

# 전체 정상
all_ok = temp_ok and pressure_ok
print("전체 정상?", all_ok)

### 실습 7
total_seconds = 98765
day_seconds = 60 * 60 * 24

days = total_seconds // day_seconds
remaining = total_seconds % day_seconds
print(days, "일")
print("나머지(초)", remaining)

hours = remaining // 3600
remaining = remaining % 3600
print(hours, "시간")
print("나머지(초)", remaining)

minutes = remaining // 60
seconds = remaining % 60
print(minutes, "분")
print(seconds, "초")

# 1일 3시간 26분 5초

######## [3] 최종 실습 #########
"""
1. 인증 코드는 SEC-로 시작해야 합니다.
2. 인증 코드의 전체 길이는 15자여야 합니다.
3. 코드의 연도는 2026이어야 합니다.
4. 마지막 문자는 X 또는 Y여야 합니다.
5. 세번째 코드의 네 자리 숫자는 1000~9999 사이여야 합니다.
6. 하이픈(-)이 정확히 3개 등장해야 합니다.
- 위의 모든 조건을 만족하는지 출력하세요.
"""
### 코드 형식 : SEC-2026-5832-X
code = "SEC-2026-5832-X"
# 1. 인증 코드는 SEC-로 시작
ch1 = code.startswith("SEC-")

# 2. 인증 코드의 전체 길이는 15
ch2 = len(code) == 15

# 3. 코드의 연도는 2026
ch3 = code[4:8] == "2026"

# 4. 마지막 문자는 X 또는 Y
ch4 = code[-1] == "X" or code[-1] == "Y"

# 5. 세번째 코드의 네 자리 숫자는 1000~9999 사이
third_code = int(code[9:13])
ch5 = third_code >= 1000 and third_code <= 9999

# 6. 하이픈(-)이 정확히 3개 등장해야 합니다.
ch6 = code.count("-") == 3

result = ch1 and ch2 and ch3 and ch4 and ch5 and ch6
print("코드로 적당한가요?", result)
