###### 간단 실습 문제 ######
# data = " EQP-01 , NORMAL , 85.5 " → "normal"
# text = " ###[ PUMP-07 ]### " → "pump_07"
# data = " TEMP / Pressure | vibration " → "temp,pressure,vibration"
log = " [WARNing] "
sensors = "temp,pressure,vibration"
data = " EQP-01 , NORMAL , 85.5 "
text = " ###[ PUMP-07 ]### "
data2 = " TEMP / Pressure | vibration "
print(log.upper()[2:9])
print(" / ".join(sensors.split(",")[::-1]).upper())
print(data.split(" , ")[1].lower())
print(text[6:13].replace("-", "_").lower())
print(data2.strip().lower().replace(" / ", ",").replace(" | ", ","))

#### 실습 4

"""
1. 생산라인 코드를 대문자·언더바 형식으로 통일
2. 생산량과 불량품 수를 정수형으로 변환
3. 가동시간 h 제거 후 정수형으로 변환
4. 각 데이터의 불량률(%) 계산
5. 2차 불량률이 1차보다 낮은지 판별
6. 전체 생산량 및 전체 불량품 수 계산
7. 통합 불량률을 전체 불량품 수 / 전체 생산량으로 계산
8. 가동시간 합산 후 시간당 평균 생산량 계산
9. 두 line이 동일 라인이며 (시간의 흐름에 따라 수집된 데이터라면 )불량률이 개선되었는지 판단
비율 및 평균은 소수점 둘째 자리까지 출력
"""
# 생산라인코드 생산략 불량품수 가동시간
line1 = " LOT-A | 1,200 | 36 | 8h "
line2 = "lot_a,850,17,5h"

parts1 = line1.split("|")
parts2 = line2.split(",")
print(parts1, parts2)

# 1. 생산라인 코드를 대문자·언더바 형식으로 통일
code1 = parts1[0].strip().upper().replace("-", "_")
code2 = parts2[0].strip().upper().replace("-", "_")
print(code1, code2)

# 2. 생산량과 불량품 수를 정수형으로 변환
total1 = int(parts1[1].strip().replace(",", ""))
total2 = int(parts2[1].strip())
print(total1, total2)

defect1 = int(parts1[2].strip())
defect2 = int(parts2[2].strip())
print(defect1, defect2)

# 3. 가동시간 h 제거 후 정수형으로 변환
hours1 = int(parts1[3].strip().replace("h", ""))
hours2 = int(parts2[3].strip().replace("h", ""))
print(hours1, hours2)

# 4. 각 데이터의 불량률(%) 계산
rate1 = defect1 / total1 * 100
rate2 = defect2 / total2 * 100
print(rate1, rate2)

# 5. 2차 불량률이 1차보다 낮은지 판별
is_improved = rate1 > rate2
print("불량률이 낮아졌나요?", is_improved)

# 6. 전체 생산량 및 전체 불량품 수 계산
total = total1 + total2
defect = defect1 + defect2

# 7. 통합 불량률을 전체 불량품 수 / 전체 생산량으로 계산
rate = defect / total * 100

# 8. 가동시간 합산 후 시간당 평균 생산량 계산
total_hours = hours1 + hours2
# 평균 생산량
hourly_avg = total / total_hours
print(f"시간당 평균생산량: {hourly_avg:.2f}")

# 9. 두 line이 동일 라인이며 시간의 흐름에 따라 수집된 데이터라면 불량률이 개선되었는지 판단
is_same_code = code1 == code2
result = is_improved and is_same_code
print(f"같은 라인이고, 불량률이 개선되었나요? {result}")

##### 실습2 #####
log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09 "
"""
1. 로그에서 날짜·시작 시각·소요시간·설비 코드 추출
2. 시작 시각을 시·분·초로 나눠 정수 변환
3. DELAY=135s에서 '135' 만 추출
4. 시작 시간을 XX시 XX분 XX초 형태로 변경
5. 완료 시간: 시작 시간에 소요 시간을 더한 후 자정 경과 여부 판단
6. 완료 시각을 시·분·초로 재계산
7. 완료 시각과 날짜 변경 여부를 f-string으로 출력
8. 날짜 자체를 다음 날로 바꿀 필요는 없음
"""
# 1. 정보 추출
parts_list = log.split("|")
print(parts_list)
date = parts_list[0].split()[0].strip()
start_time = parts_list[0].split()[1].strip()
# print(date, start_time)
delay = parts_list[1].strip()  # DELAY=135s
delay = delay.replace("DELAY=", "").replace("s", "")
delay = int(delay)
# print(delay)
code = parts_list[2].strip()
# print(code)

# 2. 시작 시각을 시·분·초로 나눠 정수 변환
time_parts_list = start_time.split(":")
print(time_parts_list)
hour = int(time_parts_list[0])
min = int(time_parts_list[1])
sec = int(time_parts_list[2])

# 4. XX시 XX분 XX초 로 변환하여 저장
time = f"{hour}시 {min}분 {sec}초"

# 5. 완료 시간: 시작 시간에 소요 시간(delay)을 더한 후 자정 경과 여부 판단
# 시작시간 23:58:45 소요시간 135초
total_seconds = hour * (60 * 60) + min * 60 + sec
# 자정이 지났으면 True
day_changed = total_seconds + delay >= (24 * 60 * 60)
print("자정이 지났나요?", day_changed)

# 6. 완료 시각을 시·분·초로 재계산
end_time = total_seconds + delay
print(end_time)

day_seconds = 24 * 60 * 60
remaining = end_time % day_seconds

end_hour = remaining // (60 * 60)
remaining = remaining % (60 * 60)

end_min = remaining // 60
end_sec = remaining % 60
print(f"최종 작업 완료 시간: {end_hour}시 {end_min}분 {end_sec}초")
