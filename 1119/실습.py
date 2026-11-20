line1 = " LOT-A | 1,200 | 36 | 8h "
line2 = "lot_a,850,17,5h"

parts1 = line1.split("|")
parts2 = line2.split(",")
# print(parts1, parts2)

# 1. 생산라인 코드를 대문자·언더바 형식으로 통일
code1 = parts1[0].strip().upper().replace("-", "_")
code2 = parts2[0].strip().upper().replace("-", "_")
if code1 == code2:
    print(f"생산라인코드:{code1}")
else:
    print("다름")
is_same_code = code1 == code2
print(f"라인코드일치: {is_same_code}")
# 2. 생산량과 불량품 수를 정수형으로 변환
total1 = int(parts1[1].strip().replace(",", ""))
total2 = int(parts2[1].strip())


defect1 = int(parts1[2].strip())
defect2 = int(parts2[2].strip())

# 4. 각 데이터의 불량률(%) 계산
rate1 = defect1 / total1 * 100
rate2 = defect2 / total2 * 100

print(f"[1차 생산] 생산량 {total1}개 / 불량품 {defect1}개")
print(f"불량률:{rate1}%")
print(f"[2차 생산] 생산량 {total2}개 / 불량품 {defect2}개")
print(f"불량률:{rate2}%")
print(f"[통합분석] 생산량 {total1+total2}개 / 불량품 {defect1+defect2}개")
print(f"불량률:{(rate1+rate2)/2}%")
# 3. 가동시간 h 제거 후 정수형으로 변환
hours1 = int(parts1[3].strip().replace("h", ""))
hours2 = int(parts2[3].strip().replace("h", ""))
# print(hours1, hours2)

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
# 5. 2차 불량률이 1차보다 낮은지 판별
is_improved = rate1 > rate2
print("불량률 개선 여부:", is_improved)
# 9. 두 line이 동일 라인이며 시간의 흐름에 따라 수집된 데이터라면 불량률이 개선되었는지 판단
is_same_code = code1 == code2
result = is_improved and is_same_code
print(f"최종판정: {result}")
