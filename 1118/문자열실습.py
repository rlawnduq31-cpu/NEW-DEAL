# 문자열 검색 종합실습
# 주어진 문자열 : NORMAL-WARNING-NORMAL-ERROR-WARNING
# 1. WARNING이 몇 번 나타나는지 출력
# 2. NORMAL이 몇 번 나타나는지 출력
# 3. ERROR이 몇 번 나타나는지 출력
# 4. 첫 번째 WARNING의 시작 위치를 구하기
# 5. 두 번째 WARNING의 시작 위치를 구하기
# 6. 첫 번째 WARNING의 끝 위치와 두 번째 WARNING의 시작 위치 사이에 몇 글자가 있는지 구하기
# 7. 두 WARNING 사이에 들어 있는 문자열만 추출하세요
# 8. 7번에서 추출한 문자열에 ERROR가 포함되어 있는지 확인

war = "NORMAL-WARNING-NORMAL-ERROR-WARNING"
# 1. WARNING이 몇 번 나타나는지 출력
print(war.count("WARNING"))
# 2. NORMAL이 몇 번 나타나는지 출력
print(war.count("NORMAL"))
# 3. ERROR이 몇 번 나타나는지 출력
print(war.count("ERROR"))
# 4. 첫 번째 WARNING의 시작 위치를 구하기
war1 = war.find("WARNING")
print(war1)
# 5. 두 번째 WARNING의 시작 위치를 구하기
war2 = war.find("WARNING", war1 + 1)
# war2 = war.rfind("WARNING")
print(war2)
# 6. 첫 번째 WARNING의 끝 위치와 두 번째 WARNING의 시작 위치 사이에 몇 글자가 있는지 구하기
first = war.find("WARNING")
second = war.find("WARNING", war1 + 1)
print(second - (first + len("WARNING")))
# 7. 두 WARNING 사이에 들어 있는 문자열만 추출하세요
bet = war[first + len("WARNING") : second]
print(bet)
# 8. 7번에서 추출한 문자열에 ERROR가 포함되어 있는지 확인
print("ERROR" in bet)

# 실습9

# 실습1
a = 17
b = 5
print(a + b, "-", a - b, "-", a * b, "-", a / b, "-", a // b, "-", a % b, "-", a**b)

# 실습2
a = 2
b = 4
c = 6
add = a + b + c
print(add)
print((a * b + b * c + c * a) * 2)
print(a * b * c)

# 실습5
error = (23 / 500) * 100
go = (21 / 24) * 100
print("불량률 ", error, "%", "-", "가동률 ", go, "%")

# 실습6
hour = 500 // 60
minutes = 500 % 60
print(hour, "시간 ", minutes, "분")

# 실습7
sec = 98765
seconds = sec % 60
minutes = (sec // 60) % 60
hour = (sec // (60 * 60)) % 24
date = sec // (24 * 3600)
print(date, "일", hour, "시간", minutes, "분", seconds, "초")

# 실습8
temp = 85
b = 5

temp1 = temp >= 60 and temp <= 90
b1 = b >= 3 and b <= 7
all = temp1 and b1
print("온도정상", temp1)
print("압력정상", b1)
print("모두정상", all)

##심화
# SEC-2026-5832-X

code = "SEC-2026-5832-X"  # input()
ch1 = code.startswith("SEC-")
ch2 = len(code) == 15
ch3 = code[4:8] == "2026"
ch4 = code[-1] == "X" or code[-1] == "Y"
third_code = int(code[9:13])
ch5 = third_code >= 1000 and third_code <= 9999
ch6 = code.count("-") == 3
result = ch1 and ch2 and ch3 and ch4 and ch5 and ch6
print("코드로 적당?", result)
